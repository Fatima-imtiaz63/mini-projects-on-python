def show_menu():
    print("\n=====NOTES MANAGER=====")
    print("1. Add a new notes")
    print("2. view all notes")
    print("3. Delete all notes")
    print("4. Exist")
def add_notes():
    notes = input("Enter your notes: " )
    with open ("notes.txt","a") as file:
        file.write(notes + "\n")
    print("Notes added successfuly!")
def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("NO notes found.")
            else:
                print("\n--- your notes---")
                
