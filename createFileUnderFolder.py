import os


directory = "TestingFolder"

if not os.path.exists(f"{directory}"):
    os.mkdir(f"{directory}")
    print(f" Directory {directory} is created")

else:
    print(f" Directory {directory} is already availabe")

print(f" Now time to create File Under the Folder {directory}")

os.chdir(f"{directory}")

create_file = "TestingFile"

with open(f"{create_file}", "w") as file:
    file.write(f" Hello This is testing file using python created")

print(f" File created under the folder")
