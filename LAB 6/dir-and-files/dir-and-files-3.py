#dir-and-files-3
import os

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

path = input("Enter the path to test: ")
test_path(path)
