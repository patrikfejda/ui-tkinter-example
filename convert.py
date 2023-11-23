import os

# Get a list of all .ui files in the ui folder
ui_files = [file for file in os.listdir("ui") if file.endswith(".ui")]

# Convert each .ui file to .py using pyuic5
for ui_file in ui_files:
    py_file = os.path.splitext(ui_file)[0] + ".py"
    py_file = py_file.replace("-", "_")
    command = f"pyuic5 -x ui/{ui_file} -o py/{py_file}"
    os.system(command)
    print(f"py/{py_file}")

print("Conversion completed.")
