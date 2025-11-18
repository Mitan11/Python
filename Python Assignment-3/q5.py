'''Write a menu-driven Python script for managing student records, allowing the user
to perform the following operations:
1. Add student details (Roll No, Name, Marks in three subjects).
2. Display all students.
3. Display student(s) whose name ends with ‘A’.
4. Display student with highest total marks.
5. Display student with lowest total marks.
6. Search student by Roll Number.
7. Sort students in descending order of total marks.
8. Exit'''

students = []

def add_student():
    roll_no = input("Enter Student Roll No: ")
    name = input("Enter Student Name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    students.append({'roll_no': roll_no, 'name': name, 'marks': marks})

def display_all_students():
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")

def display_students_name_ends_with_a():
    print("Students whose name ends with 'A':")
    for student in students:
        if student['name'].endswith('A'):
            print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")

def display_highest_total_marks():
    highest_total = 0
    top_student = None
    for student in students:
        total_marks = sum(student['marks'])
        if total_marks > highest_total:
            highest_total = total_marks
            top_student = student
    print(f"Student with Highest Total Marks: Roll No: {top_student['roll_no']}, Name: {top_student['name']}, Total Marks: {highest_total}")

def display_lowest_total_marks():
    lowest_total = float('inf')
    bottom_student = None
    for student in students:
        total_marks = sum(student['marks'])
        if total_marks < lowest_total:
            lowest_total = total_marks
            bottom_student = student
    print(f"Student with Lowest Total Marks: Roll No: {bottom_student['roll_no']}, Name: {bottom_student['name']}, Total Marks: {lowest_total}")

def search_student_by_roll_no():
    roll_no = input("Enter Student Roll No to search: ")
    for student in students:
        if student['roll_no'] == roll_no:
            print(f"Found Student: Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")
            return
    print("Student not found.")

def sort_students_by_total_marks_desc():
    sorted_students = sorted(students, key=lambda x: sum(x['marks']), reverse=True)
    print("Students sorted by Total Marks (Descending):")
    for student in sorted_students:
        total_marks = sum(student['marks'])
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Total Marks: {total_marks}")

while True:
    print("\nMenu:")
    print("1. Add student details")
    print("2. Display all students")
    print("3. Display student(s) whose name ends with ‘A’")
    print("4. Display student with highest total marks")
    print("5. Display student with lowest total marks")
    print("6. Search student by Roll Number")
    print("7. Sort students in descending order of total marks")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_all_students()
    elif choice == '3':
        display_students_name_ends_with_a()
    elif choice == '4':
        display_highest_total_marks()
    elif choice == '5':
        display_lowest_total_marks()
    elif choice == '6':
        search_student_by_roll_no()
    elif choice == '7':
        sort_students_by_total_marks_desc()
    elif choice == '8':
        print("Exiting the program.")
        break