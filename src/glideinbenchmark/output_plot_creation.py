import pandas as pd
import os
import matplotlib.pyplot as plt

output_directory = "./output"

# Read the csv files into a single dataframe
data = pd.DataFrame()
for file in os.listdir(output_directory):
    if file.endswith('.csv'):
        file_path = os.path.join(output_directory, file)
        try:
            data = pd.read_csv(file_path)

            # go through the values under the job name and put the results in a histogram
            job_names = data['job_name'].astype(str).to_list()
            results = data['result'].to_list()

            # # Create a plot using the job_names as x axis and results as y axis
            # plt.bar(job_names, results)
            plt.hist(results, bins=int(max(results)) - int(min(results)) + 1)
            plt.xlabel('Job Names')
            plt.ylabel('Results')
            plt.title(f'Job Results for {file[:-4]}')
            plt.show()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
# maybe instead of doing by job bar chart, do histogram of the results
# https://matplotlib.org/stable/gallery/user_interfaces/web_application_server_sgskip.html