def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line of text\n")
            file.write("12345\n")
            file.write("Third line with a mix of text and numbers\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Fourth line added during append operation\n")
            file.write("67890\n")
            file.write("Sixth line appended with a mix of text and numbers\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")

def main():
    create_file()
    read_file()
    append_file()

if __name__ == "__main__":
    main()
