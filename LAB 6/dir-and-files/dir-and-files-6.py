#dir-and-files-6
import string

def generate_text_files():
    alphabet = string.ascii_uppercase

    try:
        for letter in alphabet:
            filename = letter + ".txt"
            with open(filename, 'w') as file:
                file.write(f"This is file {filename}\n")
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

#call the function to generate text files
generate_text_files()
