'''
Write a menu driven python script for managing student’s result, which will allow
user to perform following operations:
1. Add Student (Which will allow user to enter the student roll no, student name,
marks of three subjects)
2. Display pass/fail status of a particular student based on following condition:
(Which will allow user to enter the student roll no and will display student’s
result)
Condition for passing the exam:
->In each subject, marks should be greater than 30 and total of any two subjects should
be greater than 70.
3. Display best 5 students as per their percentage.
4. Exit
'''

students = []

def add_student():
    roll_no = input("Enter Student Roll No: ")
    name = input("Enter Student Name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    students.append({'roll_no': roll_no, 'name': name, 'marks': marks})

def display_pass_fail():
    roll_no = input("Enter Student Roll No to check pass/fail status: ")
    for student in students:
        if student['roll_no'] == roll_no:
            marks = student['marks']
            total = sum(marks)
            if marks[0] > 30 and marks[1] > 30 and marks[2] > 30 and (marks[0] + marks[1] > 70 or marks[1] + marks[2] > 70 or marks[0] + marks[2] > 70):
                print(f"Student {student['name']} (Roll No: {roll_no}) has PASSED.")
            else:
                print(f"Student {student['name']} (Roll No: {roll_no}) has FAILED.")
            return
    print("Student not found.")

def display_best_students():
    for student in students:
        total_marks = sum(student['marks'])
        percentage = (total_marks / 300) * 100
        print(f"Student: {student['name']}, Roll No: {student['roll_no']}, Percentage: {percentage:.2f}%")


while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display pass/fail status of a particular student")
    print("3. Display best 5 students as per their percentage")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_pass_fail()
    elif choice == '3':
        display_best_students()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")