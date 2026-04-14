from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm, UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate , login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(req):
    form = UserLoginForm()
    if req.method == 'POST':
        form = UserLoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)
            if user:
                user_login(req, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")

    return render(req, "login.html" , {'form' : form})

def register(req):
    form = UserRegisterForm()
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            user_login(req , user)
            return redirect('home')
    return render(req, 'register.html' , {'form' : form})

def logout(req):
    user_logout(req)
    return redirect('home')

@login_required
def home(req):
    data = Student.objects.all()
    return render(req, 'home.html', {"data": data})


@login_required
def add(req):
    if req.method == "POST":
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req , 'form.html', {"form" : StudentForm()})


@login_required
def edit(req, id):
    student = get_object_or_404(Student, id=id)
    if req.method == "POST":
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'form.html', {"form": StudentForm(instance=student)})


@login_required
def delete(req, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')