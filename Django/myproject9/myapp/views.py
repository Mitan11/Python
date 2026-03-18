from django.shortcuts import render , redirect , get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(req):

    data = Student.objects.all()

    return render(req, "myapp/home.html",{"data" : data})

def add(req):
    if req.method == "POST":

        name = req.POST.get('name')
        age = req.POST.get('age')
        email = req.POST.get('email')
        Student.objects.create(name=name, age=age, email=email)
        return redirect('home')
    
    return render(req, "myapp/add.html" , {"form" : StudentForm()})


def edit(req, id):
    data = get_object_or_404(Student, id=id)

    if req.method == "POST":

        data.name = req.POST.get('name')
        data.age = req.POST.get('age')
        data.email = req.POST.get('email')
        data.save()

        return redirect('home')

    return render(req, "myapp/edit.html", {"data": data})

def delete(req, id):

    data = get_object_or_404(Student, id=id)
    data.delete()
    
    return redirect('home')