# SPDX-FileCopyrightText: 2023 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0

"""
This App edits the GlideinWMS Factory configuration to
enable or disable the benchmarks during the Glideins setup
"""

import os
import subprocess

from flask import Flask, render_template, request
from glideinbenchmark import factory_parser

# RUN THIS BEFORE RUNNING THE FILE export PYTHONPATH="$PYTHONPATH:/home/swamina7/GlideinBenchmark_webapp/glideinbenchmark/src/"

app = Flask(__name__)
# xml_file_dir = "/etc/gwms-factory/glideinWMS.xml"  # './xml_files' # should be /etc/gwms-factory/config.d but is xml_files temporarily
# xml_file_dir = './temp_factory.xml'
# xml_file_dir = 'temp_factory.xml'
# xml_file_dir = './testing.xml'
# xml_file_dir = '
xml_file_dir = '../../test/fixtures/etc_gwms-factory/glideinWMS.xml'
script_path = (
    factory_parser.__file__
)

app.config['XML_CONFIG'] = xml_file_dir

@app.route("/runner/config", methods=["GET", "POST"])
def runner_config():
    """
    Creates the page controlling the Factory configuration
    This function handles the runner_config route of the Flask application.
    The xml_config path is set in the Flask application's configuration before the application is run.
    """
    xml_config = app.config['XML_CONFIG']

    if xml_config.endswith(".xml") and os.path.isfile(xml_config):
        xml_files = [xml_config]
        xml_config = os.path.join(os.path.dirname(xml_config), "config.d")
    else:
        xml_files = []
    # get a list of all the xml files in the directory
    if os.path.isdir(xml_config):
        xml_files += [(xml_file_dir + f) for f in os.listdir(xml_config) if f.endswith(".xml")]
    print(xml_files)
    # set a dict to store all the entries in
    entries = {}
    # Check if there are any xml files in the directory
    if len(xml_files) == 0:
        print("No xml files found")
        return render_template("runner_config.html", entries=[])
    # go through all the xml files and get the entries in each
    for xml_file in xml_files:
        xml_name = os.path.basename(xml_file).split(".")[0]
        xml_file = os.path.abspath(xml_file)
        # check if file exists and if not, return empty list
        if factory_parser.check_file_exists(xml_file) == False:
            print(xml_file)
            print("factory location incorrect")
            return render_template("runner_config.html", entries=[])
        if request.method == "POST":
            # get the entries from the current xml file
            curr_entries = factory_parser.list_entries(xml_file=xml_file)
            enabled_entries = []
            disabled_entries = []
            removed_entries = []
            # go through each entry and get the status
            for entry in curr_entries:
                selected_option = request.form.get(f"{xml_name}_{entry}_status")
                if selected_option == "enable":
                    # Code to enable the entry
                    enabled_entries.append(entry)
                    print(f"{entry} Enable selected")
                elif selected_option == "disable":
                    disabled_entries.append(entry)
                    # Code to disable the entry
                    print(f"{entry} Disable selected")
                elif selected_option == "remove":
                    removed_entries.append(entry)
                    # Code to remove the entry
                    print(f"{entry} Remove selected")
                else:
                    print(f"No action taken for {entry}")
            # get a comma separated list of entries for each type
            if len(enabled_entries) > 0:
                enabled_entries_str = ",".join(enabled_entries)
                subprocess.call(
                    ["python3", script_path, "-e", enabled_entries_str, xml_file]
                )
            if len(disabled_entries) > 0:
                disabled_entries_str = ",".join(disabled_entries)
                subprocess.call(
                    ["python3", script_path, "-d", disabled_entries_str, xml_file]
                )
            if len(removed_entries) > 0:
                removed_entries_str = ",".join(removed_entries)
                subprocess.call(
                    ["python3", script_path, "-r", removed_entries_str, xml_file]
                )
        curr_entries = factory_parser.list_entry_status(xml_file=xml_file)
        for entry in curr_entries:
            # get file name without extension
            entry_name = xml_name + "_" + entry
            # add the entry name to the dict with entry name
            entries[entry_name] = curr_entries[entry]
        # entries = curr_entries
    return render_template("runner_config.html", entries=entries)


if __name__ == "__main__":
    app.run(debug=True)