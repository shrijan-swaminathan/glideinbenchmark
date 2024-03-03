# SPDX-FileCopyrightText: 2023 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0

import argparse
import os
import sys
import xml.etree.ElementTree as ET

"""
This parses the results from the glidein logs
"""
glidein_log_dir = '/var/log/gwms-factory/client'

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

def parse_xml_content(xml_content):
    try:
        root = ET.fromstring(xml_content)
        print("The content is a valid XML file.")
        result_element = root.find("parameter[@name='result']")
        if result_element is not None:
            result = result_element.text
            print("  The result is:", result)
        else:
            print("  Result element not found in the XML content.")
    except ET.ParseError:
        print("The content is not a valid XML file.")

def process_matching_files(directory):
    matching_files = find_matching_files(directory)
    for file in matching_files:
        print(file)
        file_path = os.path.join(directory, file)
        xml_content = extract_xml_content(file_path)
        if xml_content is not None:
            parse_xml_content(xml_content)

# Usage
process_matching_files(glidein_log_dir)
