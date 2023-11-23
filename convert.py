import os

# Get a list of all .ui files in the current directory
ui_files = [file for file in os.listdir() if file.endswith(".ui")]

# Convert each .ui file to .py using pyuic5
for ui_file in ui_files:
    py_file = os.path.splitext(ui_file)[0] + ".py"
    command = f"pyuic5 -x ui/{ui_file} -o py/{py_file}"
    os.system(command)

print("Conversion completed.")
