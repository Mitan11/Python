from django.shortcuts import redirect, render
from dbapp.models import Marks, Student

'''
# to get all data from database
data = Student.objects.all()

# to get specific data from database
data = Student.objects.get(roll=1)

# to insert data into database
student = Student.object.create(parameters)
'''

# Create your views here.
def home(req):
    data = Student.objects.all()

    return render(req , 'home.html' , {'students': data})


def add_student(req):
    msg = ''
    if req.method == 'POST':
        roll = req.POST.get('roll')
        name = req.POST.get('name')
        phone = req.POST.get('contact')
        course = req.POST.get('course')

        if Student.objects.filter(roll=roll).exists():
            msg = "Student with this roll number already exists"
            return render(req , 'add.html' , {'msg': msg})

        # marks
        cn = req.POST.get('cn')
        dbms = req.POST.get('dbms')
        python = req.POST.get('python')
        aiml = req.POST.get('aiml')
        totalMarks = int(cn) + int(dbms) + int(python) + int(aiml)
        percentage = (totalMarks / 400) * 100
        print(roll, name, phone, course, cn, dbms, python, aiml)

        student = Student.objects.create(roll=roll, name=name, phone=phone, course=course , totalMarks=totalMarks, percentage=f"{percentage:.2f}%")
        marks = Marks.objects.create(studentRoll=student, cn=cn, dbms=dbms, python=python, aiml=aiml)
        student.save()
        marks.save()

        msg = "Student added successfully"
        return redirect('home')
    return render(req , 'add.html')

def delete_student(req,roll):
    student = Student.objects.get(roll=roll)
    student.delete()
    student.save()
    return redirect('home')

def edit_student(req , roll):
    
    student = Student.objects.get(roll=roll)
    marks = Marks.objects.get(studentRoll=student)
    if req.method == 'POST':
        roll = req.POST.get('roll')
        name = req.POST.get('name')
        phone = req.POST.get('contact')
        course = req.POST.get('course')

        # marks
        cn = req.POST.get('cn')
        dbms = req.POST.get('dbms')
        python = req.POST.get('python')
        aiml = req.POST.get('aiml')
        totalMarks = int(cn) + int(dbms) + int(python) + int(aiml)
        percentage = (totalMarks / 400) * 100
        print(roll, name, phone, course, cn, dbms, python, aiml)

        student.roll = roll
        student.name = name
        student.phone = phone
        student.course = course

        marks.cn = cn
        marks.dbms = dbms
        marks.python = python
        marks.aiml = aiml
        student.totalMarks = totalMarks
        student.percentage = f"{percentage:.2f}%"
        student.save()
        marks.save()

        msg = "Student updated successfully"
        return redirect('home')

    return render(req , 'edit.html', {'student': student, 'marks': marks})

def view_result(req, roll):
    student = Student.objects.get(roll=roll)
    marks = Marks.objects.get(studentRoll=student)

    return render(req , 'marksheet.html', {'student': student, 'marks': marks})