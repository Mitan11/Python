from django.shortcuts import render, redirect

students = [
    {
        "roll": 1,
        "name": "Mitan Tank",
        "contact": 321654970,
        "course": "MscIT",
        "marks": {"Python": 90, "DAD": 90, "CSCL": 90},
        "totalMarks": 270,
        "percentage": "90%"
    },
    {
        "roll": 2,
        "name": "Rahul Sharma",
        "contact": 987654321,
        "course": "MscIT",
        "marks": {"Python": 85, "DAD": 88, "CSCL": 92},
        "totalMarks": 265,
        "percentage": "88.33%"
    },
    {
        "roll": 3, 
        "name": "Priya Patel",
        "contact": 912345678,
        "course": "MscIT",
        "marks": {"Python": 95, "DAD": 91, "CSCL": 94},
        "totalMarks": 280,
        "percentage": "93.33%"
    },
    {
        "name": "Aman Verma",
        "roll": 4, 
        "contact": 998877665,
        "course": "MscIT",
        "marks": {"Python": 78, "DAD": 82, "CSCL": 80},
        "totalMarks": 240,
        "percentage": "80%"
    },
    {
        "roll": 5,
        "name": "Neha Singh",
        "contact": 909090909,
        "course": "MscIT",
        "marks": {"Python": 88, "DAD": 90, "CSCL": 85},
        "totalMarks": 263,
        "percentage": "87.67%"
    }
]

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html' , {'students': students})

def add_student(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        course = request.POST.get('course')

        # Check if roll number already exists
        for student in students:
            if int(student['roll']) == int(roll):
                error_message = f"Roll number {roll} already exists!"
                return render(request, 'myapp/add.html', {'error': error_message})

        student = {
            "roll": roll,
            "name": name,
            "contact": contact,
            "course": course,
            "marks": {},
            "totalMarks": 0,
            "percentage": "0%"
        }
        students.append(student)

        return redirect('home')
    return render(request, 'myapp/add.html')

def edit_student(request, roll):
    if request.method == 'POST':
        
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        course = request.POST.get('course')

        for student in students:
            if student['roll'] == int(roll):
                student['name'] = name
                student['contact'] = contact
                student['course'] = course
                break

        return redirect('home')
    for student in students:
        if student['roll'] == roll:
            context = {'student': student}
            return render(request, 'myapp/edit.html', context)

def delete_student(request, roll):

    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            break

    return redirect('home')