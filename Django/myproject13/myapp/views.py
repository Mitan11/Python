from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, EmpForm
from .models import Employee

# Create your views here.
def home(req):
    data = Employee.objects.all()
    return render(req , "home.html", {"data" : data, "show_logout": req.user.is_authenticated})

@login_required
def add(req):

    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        email = req.POST.get('email')
        doj = req.POST.get('date_of_join')
        Employee.objects.create(name = name , age = age , email = email , date_of_join = doj)
        return redirect("home")
        
    return render(req , 'add.html' , {"form" : EmpForm()})

@login_required
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

@login_required
def delete(req, id):
    data = get_object_or_404(Employee , id = id)
    data.delete()
    return redirect("home")

def login(req):
    form = UserLoginForm()
    if req.method == 'POST':
        form = UserLoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user:
                auth_login(req, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    return render(req , 'login.html' , {'form' : form})


def logout(req):
    auth_logout(req)
    return redirect('login')