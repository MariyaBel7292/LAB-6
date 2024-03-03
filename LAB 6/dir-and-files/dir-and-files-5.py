#dir-and-files-5
def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(item + '\n')
        print(f"List written to {filename} successfully.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
