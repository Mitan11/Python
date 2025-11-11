'''Perform following in python using the concept of list:
Create different four list with the name: StudentName, marks_math, marks_science,
marks_english
Take five input from user for each list.
Create a menu and perform following on created lists:
1. Display all students details in tabular form: Name, Math, Science, English.
2. Calculate the total marks for each student and store in a list total_marks.
3. Find the student with the highest total marks and display.
4. Exit
'''

student_names = []
marks_math = []
marks_science = []
marks_english = []

# Taking user input for student details
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    math_marks = float(input(f"Enter Math marks for {name}: "))
    science_marks = float(input(f"Enter Science marks for {name}: "))
    english_marks = float(input(f"Enter English marks for {name}: "))
    
    student_names.append(name)
    marks_math.append(math_marks)
    marks_science.append(science_marks)
    marks_english.append(english_marks)

while True:
    print("\nMenu:")
    print("1. Display all students details in tabular form: Name, Math, Science, English")
    print("2. Calculate the total marks for each student and store in a list total_marks")
    print("3. Find the student with the highest total marks and display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nStudent Details:")
        print("Name\tMath\tScience\tEnglish")
        for i in range(len(student_names)):
            print(f"{student_names[i]}\t{marks_math[i]}\t{marks_science[i]}\t{marks_english[i]}")

    elif choice == '2':
        total_marks = []
        for i in range(len(student_names)):
            total = marks_math[i] + marks_science[i] + marks_english[i]
            total_marks.append(total)
        print("Total marks calculated and stored in total_marks list.")

    elif choice == '3':
        highest_marks = max(total_marks)
        index = total_marks.index(highest_marks)
        print(f"Student with highest total marks: {student_names[index]} with {highest_marks} marks.")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")