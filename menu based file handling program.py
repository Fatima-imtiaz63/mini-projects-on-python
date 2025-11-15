def write_file():
    file = open("mydata.txt","w")
    text = input("Enter text to write in file: ")
    file.write(text +"\n")
    file.close()
    print("Data written successfully!\n")
def read_file():
    file = open("mydata.txt","r")
    content = file.read()
    if content == "":
        print("\nFile is empty! \n")
    else:
        print("\n File content:\n"+ content +"\n")
        file.close()
        
print("File not found! Write something first. \n")
def append_file():
    file = open("mydata.txt","a")
    text =input("Enter text to append:")
    file.write("\n" + text)
    file.close()
    print("Data appened successfully! \n")

while True:
    print("===FILE HANDLING MENU===")
    print("1. Write to file")
    print("2.Read file")
    print("3. Appened to file")
    print("3.Exit")
    choice = input("Enter your choice(1-4);")
    if choice =="1":
        write_file()
    elif choice =="2":
        read_file()
    elif choice =="3":
        append_file()
    elif choice =="4":
        print("Exiting program. Goodbye")
        break
    else:
        print("Invalid choice! please select 1-4.\n")
write_file()
read_file()
append_file()
