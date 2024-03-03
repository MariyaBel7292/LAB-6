#dir-and-files-2
import os

def check_path_access(path):
    if os.path.exists(path):
        print("Path exists.")

        if os.access(path, os.R_OK):
            print("Readable: Yes")
        else:
            print("Readable: No")

        if os.access(path, os.W_OK):
            print("Writable: Yes")
        else:
            print("Writable: No")

        if os.access(path, os.X_OK):
            print("Executable: Yes")
        else:
            print("Executable: No")

    else:
        print("Path does not exist.")

path = input("Enter the path to check: ")
check_path_access(path)
