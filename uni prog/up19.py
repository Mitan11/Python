students = []

def addStudent():
    name = input("Enter your name: ")
    roll = int(input("Enter your roll number: "))
    contact = list(map(int, input("Enter contact numbers separated by spaces: ").split()))
    
    marks = {}
    subject = ["Python", "DAD", "CSCL"]
    total = 0
    
    for sub in subject:
        marks[sub] = int(input(f"Enter {sub} marks out of 100 : "))
        total += marks[sub]
    
    percentage = (total / (len(subject) * 100)) * 100
    print(f"Total marks: {total}")
    print(f"Percentage: {percentage:.2f}%")

    highest_subject = max(marks, key=marks.get)
    lowest_subject = min(marks, key=marks.get)
    print(f"Highest marks in: {highest_subject} ({marks[highest_subject]})")
    print(f"Lowest marks in: {lowest_subject} ({marks[lowest_subject]})")

    students.append({
        "name": name,
        "roll": roll,
        "contact": contact,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "highest_subject": highest_subject,
        "lowest_subject": lowest_subject
    })

def studentMarks(roll):
	for i in students:
		if roll == i["roll"]:
			return [i["total"] , i["percentage"]]

while True:

	print("Press 1 to add student")
	print("Press 2 to display student")
	print("Press 3 to display any student marks")
	print("Press 4 to exit")

	choice = int(input("Enter your choice : "))\

	if choice == 1:
		addStudent()

	elif choice == 2:
		print(students)
	
	elif choice == 3:
		student = int(input("Enter student roll number to find marks : "))
		total , percentage = studentMarks(student)
		print(f"Total marks is {total} and percentage is {percentage:.2f}%")

	elif choice == 4:
		exit()

	else:
		print("Invalid Choice")
