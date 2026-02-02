from django.shortcuts import redirect, render
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

# This view shows the home page with a form to enter roll number
def home(request):
    return render(request, 'home.html')

def student_list(request):
    return render(request, 'studentlist.html', {"students" : students})

def addStudent(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        roll = int(request.POST.get('roll'))
        contact = int(request.POST.get('contact'))
        python_marks = int(request.POST.get('python'))
        dad_marks = int(request.POST.get('dad'))
        cscl_marks = int(request.POST.get('cscl'))

        total_marks = python_marks + dad_marks + cscl_marks
        percentage = (total_marks / 300) * 100

        if roll in [student["roll"] for student in students]:
            error_message = f"Student with Roll Number {roll} already exists."
            return render(request, 'addstudent.html', {'error': error_message})

        new_student = {
            "name": name,
            "roll": roll,
            "contact": contact,
            "marks": {
                "Python": python_marks,
                "DAD": dad_marks,
                "CSCL": cscl_marks
            },
            "totalMarks": total_marks,
            "percentage": f"{percentage:.2f}%"
        }

        students.append(new_student)

        return redirect('student_list')

    return render(request, 'addstudent.html')


# This view processes the roll number and shows the marksheet
def get_marksheet(request , roll_number=None):
    # Sample student data (in real projects, this comes from database)

    if roll_number is not None:
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
