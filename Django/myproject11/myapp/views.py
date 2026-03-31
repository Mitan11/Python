from django.shortcuts import render , redirect , get_object_or_404
from .models import Employee
from .forms import EmpForm

# Create your views here.
def home(req):

    data = Employee.objects.all()

    return render(req , "home.html", {"data" : data})


def add(req):

    if req.method == 'POST':

        name = req.POST.get('name')
        age = req.POST.get('age')
        email = req.POST.get('email')
        doj = req.POST.get('date_of_join')

        Employee.objects.create(name = name , age = age , email = email , date_of_join = doj)
        
        return redirect("home")
        
    return render(req , 'add.html' , {"form" : EmpForm()})

def edit(req, id):
    data = get_object_or_404(Employee , id = id)

    if req.method == 'POST':

        data.name = req.POST.get('name')
        data.age = req.POST.get('age')
        data.email = req.POST.get('email')
        data.date_of_join = req.POST.get('date_of_join')

        data.save()
        
        return redirect("home")

    return render(req , 'add.html' , {"form" : EmpForm(instance=data)})

def delete(req, id):

    data = get_object_or_404(Employee , id = id)

    data.delete()

    return redirect("home")