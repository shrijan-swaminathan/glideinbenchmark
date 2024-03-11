import os
import xml.etree.ElementTree as ET
import csv

directory = "./"
output_directory = "./output"

def find_matching_files(directory):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("job.") and file.endswith(".err"):
                matching_files.append(os.path.join(root, file))
    return matching_files

def extract_xml_content(file_path):
    with open(file_path, "r") as f:
        contents = f.readlines()
        start_index = None
        end_index = None
        for i, line in enumerate(contents):
            if line.strip() == "==== GlideinBenchmark results ====":
                start_index = i + 1
            elif line.strip() == "==== GlideinBenchmark end ====":
                end_index = i
                break
        if start_index is not None and end_index is not None:
            xml_content = "".join(contents[start_index:end_index])
            return xml_content
        else:
            return None

def xml_content_to_csv(xml_content, output_directory, job_name):
    try:
        print(job_name)
        # get the root into an Etree
        root = ET.fromstring(xml_content)
        # Find the name associated with the main class
        name = None
        csv_file = os.path.join(output_directory, "")  # Add output_directory to csv_file path
        data = {"job_name": job_name}  # Add job_name as the first column
        for element in root:
            if element.tag == "bmk_name":
                name = element.text
            if element.text is not None and element.tag != "bmk_name":
                data[element.tag] = element.text

        # Check if a name is found and print the result
        if name is None:
            print("Invalid")
            return False
        else:
            print("Name:", name)
            csv_file += name + ".csv"
        # Check if the csv file exists
        file_exists = os.path.isfile(csv_file)
        # Read the existing data from the csv file
        existing_data = []
        if file_exists:
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                existing_data = list(reader)
        # Update the existing row if job_name already exists
        for row in existing_data:
            if row["job_name"] == job_name:
                row.update(data)
        # Write the content of the xml file to the csv file
        with open(csv_file, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writeheader()
            writer.writerows(existing_data)
        # Append the data if job_name doesn't exist in the csv file
        if not any(row["job_name"] == job_name for row in existing_data):
            with open(csv_file, 'a') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writerow(data)
    except ET.ParseError:
        print("The content is not a valid XML file.")

def process_matching_files(directory):
    matching_files = find_matching_files(directory)
    for file in matching_files:
        # print(file)
        file_path = os.path.join(directory, file)
        xml_content = extract_xml_content(file_path)
        if xml_content is not None:
            # remove every value before the last / and add the output directory
            job_name = os.path.basename(file)[4:-4]
            xml_content_to_csv(xml_content, output_directory, job_name)

if __name__ == "__main__":
    # Usage
    process_matching_files(directory)
