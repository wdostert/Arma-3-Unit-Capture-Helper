import os

file_name = "init.sqf"

# Ask user for unit name
unit_name = input("Enter the unit name: ")

# Read existing content if the file exists
try:
    with open(file_name, "r") as file:
        lines = file.readlines()
        last_index = 1
        for line in lines:
            if line.startswith("Path"):
                last_index += 1
except FileNotFoundError:
    last_index = 1

new_line = f"\nPath{last_index} = compile preprocessFile \"path{last_index}.sqf\";\n"

# Append the new line to the file
with open(file_name, "a") as file:
    file.write(new_line)

# Ask user to paste the path data
path_data = input(f"Paste the path data for Path{last_index}: ")

# Create the corresponding path file in the current directory
path_file_name = f"path{last_index}.sqf"
path_content = f"Path{last_index} = {path_data};\n[{unit_name}, Path{last_index}] spawn BIS_fnc_UnitPlay;"

with open(path_file_name, "w") as path_file:
    path_file.write(path_content)

# Provide a message for the user to copy
rec_message = f"rec{last_index} = [] spawn Path{last_index}"

print(f"File '{file_name}' has been updated with: {new_line.strip()}")
print(f"File '{path_file_name}' has been created with the provided path data using unit '{unit_name}'.")
print(f"Copy the following message: \n{rec_message};")

# Wait for user to press Enter before closing
input("Press Enter to exit...")
