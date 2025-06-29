from pathlib import Path

def readFileAndFolder():
    path = Path('.') 
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def create_file():
    try:
        readFileAndFolder()
        name = input("Please tell your file name : ")
        p = Path(name)
        if not p.exists(): 
            with open(p, "w") as fs:
                data = input("What you want to write in this file : ")
                fs.write(data)
            print("File created successfully")
        else:
            print("This file already exists")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        readFileAndFolder()
        name = input("Which file you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(f"\nFile contents:\n{data}")
        else:
            print("File doesn't exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_file():
    try:
        readFileAndFolder()
        name = input("Which file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file() :
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending content in your file")

            res = int(input("tell your response : "))
            if res == 1:
                name2 = input("tell your new file name : ")
                p2 = Path(name2)
                p.rename(p2)
            elif res == 2:
                with open(p , 'w') as fs:
                    data = input("What you want to write this will overrite the data : ")
                    fs.write(data)
            elif res == 3:
                with open(p , 'a') as fs:
                    data = input("What you want to append : ")
                    fs.write(" " + data)
    except Exception as e :
        print(f"Error occured as  : {e}")

def delete_file():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete : ")
        p = Path(name)
        if p.exists() and p.is_file():
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")
            if confirm.lower() in ['yes', 'y']:
                p.unlink()
                print("File deleted successfully")
            else:
                print("File deletion cancelled")
        else:
            print("File doesn't exist")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Press 1 for Creating a new file")
print("Press 2 for reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deleting a file")


choice = int(input("\nEnter your choice: "))
            
if choice == 1:
    create_file()
elif choice == 2:
    read_file()
elif choice == 3:
    update_file()
elif choice == 4:
    delete_file()
else:
    print("Invalid choice. Please enter a number between 1-5.")
        

