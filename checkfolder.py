import os

#Want to check folder are exiting or not if not avlaible then create

#folder = os.path.dirname(/home/cadet/Desktop/studio)

#create_folder =os.path.exists(/home/cadet/Desktop/studio)


directory = "/home/cadet/Desktop/studio"

try :
    os.mkdir(directory)
    print(f" Directory '{directory}' path is created")
except FileExistsError:
    print(f"Directory '{directory}' is already exiting")
except PermissionError:
    print(f" Due to permission error not created")
except Exception as e:
    print(f" An error occurred {e}")
