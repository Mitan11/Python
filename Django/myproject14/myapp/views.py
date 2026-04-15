from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm , UserLoginForm , UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as as_login , logout as as_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(req):
    
    form = UserLoginForm()

    if req.method == 'POST':
        form = UserLoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(req , username = username , password = password)

            if user:
                as_login(req, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")

    return render(req, 'login.html', {'form' : form})

def register(req):

    form = UserRegistrationForm()

    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            as_login(req, user)
            return redirect('home')

    return render(req, 'register.html' , {'form' : form})

def logout(req):
    as_logout(req)
    return redirect('login')

@login_required
def home(req):

    data = Student.objects.all()

    return render(req, 'home.html' , {'data' : data})

@login_required
def add(req):

    form = StudentForm()

    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(req, 'form.html', {'form' : form})

@login_required
def edit(req, id):
    
    data = get_object_or_404(Student , id = id)
    form = StudentForm(instance=data)
    if req.method == 'POST':
        form = StudentForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(req, 'form.html' , {'form' : form , 'isEdit' : True })

@login_required
def delete(req , id):
    
    data = get_object_or_404(Student , id = id)
    data.delete()

    return redirect('home')