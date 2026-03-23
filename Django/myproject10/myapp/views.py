from django.shortcuts import render , redirect, get_object_or_404
from .models import Employee
from .forms import EmployeesForm

# Create your views here.
def home(req):
    data = Employee.objects.all()
    print(data)
    return render(req, 'home.html' , {'data': data})

def add(req):

    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        department = req.POST.get('department')
        date_of_joining = req.POST.get('date_of_joining')
        Employee.objects.create(name=name , email=email , department=department , date_of_joining=date_of_joining)
        return redirect('home')

    return render(req, 'add.html' , {"form": EmployeesForm()})

def edit(req , id):
    data = get_object_or_404(Employee , id=id)

    if req.method == 'POST':
        data.name = req.POST.get('name')
        data.email = req.POST.get('email')
        data.department = req.POST.get('department')
        data.date_of_joining = req.POST.get('date_of_joining')
        data.save()
        return redirect('home')

    return render(req, 'add.html' , {"form" : EmployeesForm(instance=data)})

def delete(req , id):
    data = get_object_or_404(Employee , id=id)
    data.delete()
    return redirect('home')

