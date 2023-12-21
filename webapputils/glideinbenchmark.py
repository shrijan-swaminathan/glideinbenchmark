from flask import Flask, render_template, request
import subprocess
import factory_parser
import os
app = Flask(__name__)
xml_file_dir = './xml_files' # should be /etc/gwms-factory/config.d but is xml_files temporarily
script_path = './factory_parser.py' #will update this for absolute path later
# xml_file = 'temp_factory.xml'


@app.route("/", methods=["GET", "POST"])
def index():
    # get a list of all the xml files in the directory
    xml_files = [f for f in os.listdir(xml_file_dir) if f.endswith('.xml')]
    # set a dict to store all the entries in
    entries = {}
    # Check if there are any xml files in the directory 
    if len(xml_files) == 0:
        print("No xml files found")
        return render_template("index.html", entries=[])
    # go through all the xml files and get the entries in each
    for xml_file in xml_files:
        xml_name = xml_file.split('.')[0]
        xml_file = os.path.join(xml_file_dir, xml_file)
        # check if file exists and if not, return empty list
        if factory_parser.check_file_exists(xml_file) == 0:
            print("factory location incorrect")
            return render_template("index.html", entries=[])
        if request.method == "POST":
            # get the entries from the current xml file
            curr_entries = factory_parser.list_entries(xml_file=xml_file)
            enabled_entries = []
            disabled_entries = []
            removed_entries = []
            # go through each entry and get the status
            for entry in curr_entries:
                selected_option = request.form.get(f'{xml_name}_{entry}_status')
                if selected_option == 'enable':
                    # Code to enable the entry
                    enabled_entries.append(entry)
                    print(f'{entry} Enable selected')
                elif selected_option == 'disable':
                    disabled_entries.append(entry)
                    # Code to disable the entry
                    print(f'{entry} Disable selected')
                elif selected_option == 'remove':
                    removed_entries.append(entry)
                    # Code to remove the entry
                    print(f'{entry} Remove selected')
                else:
                    print(f'No action taken for {entry}')
            # get a comma separated list of entries for each type
            if len(enabled_entries) > 0:
                enabled_entries_str = ','.join(enabled_entries)
                subprocess.call(['python3', script_path, '-e', enabled_entries_str, xml_file])
            if len(disabled_entries) > 0:
                disabled_entries_str = ','.join(disabled_entries)
                subprocess.call(['python3', script_path, '-d', disabled_entries_str, xml_file])
            if len(removed_entries) > 0:
                removed_entries_str = ','.join(removed_entries)
                subprocess.call(['python3', script_path, '-r', removed_entries_str, xml_file])
        curr_entries = factory_parser.list_entry_status(xml_file=xml_file)
        for entry in curr_entries:
            # get file name without extension
            entry_name = xml_name + '_' + entry
            # add the entry name to the dict with entry name
            entries[entry_name] = curr_entries[entry]
        # entries = curr_entries
    return render_template("index.html", entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
    index()