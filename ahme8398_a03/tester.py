import subprocess

# Information about the author
author = "Ali Ahmed"
ID = "169038398"
email = "ahme8398@mylaurier.ca"
version = "2023-01-28"

# Open the file to write the output
with open("testing.txt", "w") as file:
    file.write("-------------------------------------------------------\n")
    file.write("Lab/Assignment Testing\n")
    file.write("-------------------------------------------------------\n")
    file.write(f"Author: {author}\n")
    file.write(f"ID: {ID}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Version: {version}\n")
    file.write("-------------------------------------------------------\n")

    # Loop through the files to test
    for i in range(1, 6+1):
        file.write(f"t0{i}\n")
        file.write("-------------------------------------------------------\n")
        result = subprocess.run(["python", "ahme8398/src/t0{i}.py".format(i=i)], stdout=subprocess.PIPE)
        file.write(result.stdout.decode("utf-8"))
        file.write("\n")
