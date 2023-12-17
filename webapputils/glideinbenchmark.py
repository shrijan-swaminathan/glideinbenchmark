from flask import Flask, render_template, request
import subprocess
import factory_parser
app = Flask(__name__)
script_path = './factory_parser.py' #will update this for absolute path later
xml_file = 'temp_factory.xml'

# add config file path
# global put on top, and add entries for all other files, in /etc/gwms-factory/config.d. Parse these together

@app.route("/", methods=["GET", "POST"])
def index():
    # check if file exists and if not, return empty list
    if factory_parser.check_file_exists(xml_file) == 0:
        print("factory location incorrect")
        return render_template("index.html", entries=[])
    if request.method == "POST":
        entries = factory_parser.list_entries(xml_file=xml_file)
        enabled_entries = []
        disabled_entries = []
        removed_entries = []
        for entry in entries:
            selected_option = request.form.get(f'{entry}_status')
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
    entries = factory_parser.list_entry_status(xml_file=xml_file)
    return render_template("index.html", entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
    index()