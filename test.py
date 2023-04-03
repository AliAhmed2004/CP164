import os

num_files = int(input("Enter the number of files you want to create: "))

path = os.path.dirname(os.path.abspath(__file__))

for i in range(1, num_files + 1):
    filename = os.path.join(path, "t" + str(i).zfill(2) + ".py")

    with open(filename, "w") as file:
        file.write("""
\"\"\"
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-09"
-------------------------------------------------------
\"\"\"
# Imports

# Constants

def func():
    \"\"\"
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    \"\"\"
        """)

print("Created", num_files, "files.")

print("Current working directory:", os.getcwd())
print("Files in the current directory:", os.listdir(path))

print("Full path of the file:", os.path.abspath(filename))