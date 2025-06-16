import os
import shutil

copy_file = "/home/cadet/Desktop/Daily Code/CICD/vpc.tf"

directory = "Config Folder"

newvpc = "newvpc"

try:
    if not os.path.exists(f" { directory}"):
        os.mkdir(f"{directory}")
        print(f"New Created Folder is {directory}")
except FileExistsError:
    print(f"Folder {directory} already exit")
except Exception as e:
    print(f"An error occurred: {e}")



os.chdir(f"{directory}")


with open(f"{newvpc}", "w") as file:
    pass


shutil.copy(copy_file, newvpc)

old_ip = "192.168"                   #"192.168.0.0"

new_ip =  "193.168"                  #"193.168.0.0"


def replace_word_in_file(newvpc, old_ip, new_ip):
    try:
        with open(newvpc, 'r') as file:
            content = file.read()

        updated_content = content.replace(old_ip, new_ip)

        with open(newvpc, 'w') as file:
            file.write(updated_content)
        print(f"Successfully replaced '{old_ip}' with '{new_ip}' in '{newvpc}'")

    except FileNotFoundError:
        print(f"Error: File not found at '{newvpc}'")

    except Exception as e:
        print(f"An error occurred: {e}")

replace_word_in_file(newvpc, old_ip, new_ip)