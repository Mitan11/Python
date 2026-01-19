from django.shortcuts import render

# This view shows the home page with a form to enter roll number
def home(request):
    return render(request, 'home.html')

# This view processes the roll number and shows the marksheet
def get_marksheet(request):
    # Sample student data (in real projects, this comes from database)
    students = [
        {
            "name": "Mitan Tank",
            "roll": 1,
            "contact": 321654970,
            "marks": {"Python": 90, "DAD": 90, "CSCL": 90},
            "totalMarks": 270,
            "percentage": "90%"
        },
        {
            "name": "Rahul Sharma",
            "roll": 2,
            "contact": 987654321,
            "marks": {"Python": 85, "DAD": 88, "CSCL": 92},
            "totalMarks": 265,
            "percentage": "88.33%"
        },
        {
            "name": "Priya Patel",
            "roll": 3,
            "contact": 912345678,
            "marks": {"Python": 95, "DAD": 91, "CSCL": 94},
            "totalMarks": 280,
            "percentage": "93.33%"
        },
        {
            "name": "Aman Verma",
            "roll": 4,
            "contact": 998877665,
            "marks": {"Python": 78, "DAD": 82, "CSCL": 80},
            "totalMarks": 240,
            "percentage": "80%"
        },
        {
            "name": "Neha Singh",
            "roll": 5,
            "contact": 909090909,
            "marks": {"Python": 88, "DAD": 90, "CSCL": 85},
            "totalMarks": 263,
            "percentage": "87.67%"
        }
    ]

    # Check if form was submitted (POST request)
    if request.method == 'POST':
        # Get the roll number from the form
        roll_number = int(request.POST.get('roll_number'))
        
        # Find student with matching roll number
        student_data = None
        for student in students:
            if student["roll"] == roll_number:
                student_data = student
                break
        
        # If student found, show marksheet
        if student_data:
            return render(request, 'marksheet.html', {'student': student_data})
        # If student not found, show error message
        else:
            error_message = f"Student with Roll Number {roll_number} not found."
            return render(request, 'home.html', {'error': error_message})
    
    # If no form submitted, show the home page
    else:
        return render(request, 'home.html')
    
'''
print("Hello World in Python")

students = [
    {
        "name": "Mitan Tank",
        "roll": 1,
        "contact": 321654970,
        "marks": {"Python": 90, "DAD": 90, "CSCL": 90},
        "totalMarks": 270,
        "percentage": "90%"
    },
    {
        "name": "Rahul Sharma",
        "roll": 2,
        "contact": 987654321,
        "marks": {"Python": 85, "DAD": 88, "CSCL": 92},
        "totalMarks": 265,
        "percentage": "88.33%"
    },
    {
        "name": "Priya Patel",
        "roll": 3,
        "contact": 912345678,
        "marks": {"Python": 95, "DAD": 91, "CSCL": 94},
        "totalMarks": 280,
        "percentage": "93.33%"
    },
    {
        "name": "Aman Verma",
        "roll": 4,
        "contact": 998877665,
        "marks": {"Python": 78, "DAD": 82, "CSCL": 80},
        "totalMarks": 240,
        "percentage": "80%"
    },
    {
        "name": "Neha Singh",
        "roll": 5,
        "contact": 909090909,
        "marks": {"Python": 88, "DAD": 90, "CSCL": 85},
        "totalMarks": 263,
        "percentage": "87.67%"
    }
]

while True:
    print("\nPress 1 to display students")
    print("Press 2 to display any student marks")
    print("Press 3 to exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(students)

    elif choice == 2:
        roll = int(input("Enter student roll number to find marks: "))
        found = False

        for i in students:
            if i["roll"] == roll:
                found = True
                print(i)
                break

        if not found:
            print("Student not found!")

    elif choice == 3:
        print("Exited")
        break

    else:
        print("Invalid Choice")

'''