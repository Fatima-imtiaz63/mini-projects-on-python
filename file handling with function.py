def write_file():
    file = open("mydata.txt", "w")
    file.write("Hello this is a file created in a using python.\n")
    file.write("We are learning file handling from function.\n")
    file.close()
    print("Data written successfully!")
def read_file():
    file = open("mydata.txt", "r")
    content = file.read()
    print("\nFile content:\n" + content)
    file.close()
def append_file():
    file = open("mydata.txt", "a")
    file.write("\n This is a line is newly added to the file.")
    file.close()
    print("Data appended successfully!")

write_file()
read_file()
append_file()