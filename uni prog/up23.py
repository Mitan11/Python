class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = []

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def getData(self):
        self.name = input("Enter Student Name: ")
        self.roll_no = int(input("Enter Roll Number: "))
        num_subjects = int(input("Enter number of subjects: "))
        
        for i in range(num_subjects):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)


students = []

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        student = Student()
        student.getData()
        students.append(student)

    elif choice == 2:
        for student in students:
            student.display_info()
            print("-" * 20)

    elif choice == 3:
        roll_no = int(input("Enter Roll Number to search: "))
        
        for student in students:
            if student.roll_no == roll_no:
                student.display_info()
                break
            else:
                print("Student not found.")
    
    elif choice == 4:
        print("Exiting...")
        break

