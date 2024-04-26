import matplotlib.pyplot as plt
import pandas as pd
import os

output_directory = "../../test/fixtures/job_logs_location/output_db"

def create_histogram():
    # Read the csv files into a single dataframe
    data = pd.DataFrame()
    figures = []  # List to store all figures
    figure_locations = []
    for file in os.listdir(output_directory):
        if file.endswith('.csv'):
            file_path = os.path.join(output_directory, file)
            figure_locations.append(os.path.abspath(file_path))
            try:
                data = pd.read_csv(file_path)
                # go through the values under the job name and put the results in a histogram
                results = data['result'].to_list()

                # Create a plot using the job_names as x axis and results as y axis
                fig, ax = plt.subplots()
                ax.hist(results, bins=int(max(results)) - int(min(results)) + 1)
                ax.set_xlabel('Values')
                ax.set_ylabel('Results')
                ax.set_title(f'Job Results for {file[:-4]}')

                figures.append(fig)  # Append the figure to the list

            except FileNotFoundError:
                print(f"File not found: {file_path}")
    return figures, figure_locations