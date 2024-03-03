#dir-and-files-8
import os

def delete_file(path):
    try:
        if os.path.exists(path):
            if os.access(path, os.W_OK):
                os.remove(path)
                print(f"File '{path}' deleted successfully.")
            else:
                print(f"No write access to '{path}'. Cannot delete the file.")
        else:
            print(f"File '{path}' does not exist.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

