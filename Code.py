def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("The answer is 42.\n")
            file.write("Python is awesome!\n")
        print("File created successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to create the file.")
    except Exception as e:
        print(f"An unexpected error occurred while creating the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This line is appended.\n")
            file.write("The current year is 2024.\n")
            file.write("File handling is important in programming.\n")
        print("Content appended successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

def main():
    print("1. Creating file...")
    create_file()

    print("\n2. Reading file contents...")
    read_file()

    print("\n3. Appending to file...")
    append_to_file()

    print("\n4. Reading updated file contents...")
    read_file()

if __name__ == "__main__":
    main()