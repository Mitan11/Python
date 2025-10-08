students = []

def addStudent():
	name = input("Enter your name : ")
	roll = int(input("Enter your roll number : "))
	contact = list(map(int, input("Enter contact number separated by spaces : ").split()))
	marks = {}
	subject = ["Python" , "DAD" , "CSCL"]
	for i in subject:
		marks[i] = int(input(f"Enter {i} marks : "))
	
	students.append({"name" : name , "roll" : roll , "contact" : contact , "marks" : marks})

def studentMarks(roll):
	total = 0
	for i in students:
		if roll == i["roll"]:
			print(f"roll number {roll} marks is", i["marks"])
			total = sum(i["marks"].values())
			print("Total marks is", total)
			percentage = (total / len(i["marks"]) * 100) * 100
			print("Percentage is", percentage)


def min_marks():
	pass

def max_marks():
	pass

while True:

	print("Press 1 to add student")
	print("Press 2 to display student")
	print("Press 3 to display any student marks")
	print("Press 4 to exit")

	choice = int(input("Enter your choice : "))

	if choice == 1:
		addStudent()

	elif choice == 2:
		print(students)
	
	elif choice == 3:
		student = int(input("Enter student roll number to find marks : "))
		studentMarks(student)

	elif choice == 4:
		exit()

	else:
		print("Invalid Choice")
