from django.shortcuts import render, redirect, get_object_or_404
from .models import Inverntory
from .forms import InventoryForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def userLogin(req):
    form = LoginForm()
    
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
            
    return render(req, 'login.html', {"form": form})

def userRegister(req):
    form = RegisterForm()
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    return render(req, 'register.html', {"form": form})

def userLogout(req):
    logout(req)
    return redirect('login')

@login_required
def home(req):

    data = Inverntory.objects.all()

    return render(req, 'home.html' , {"data": data})

@login_required
def add(req):
    if req.method == "POST":
        form = InventoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req , 'form.html' , {"form" : InventoryForm()})
    
@login_required
def edit(req, id):
    data = get_object_or_404(Inverntory, id=id)
    if req.method == "POST":
        form = InventoryForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InventoryForm(instance=data)
    return render(req, 'form.html', {"form": form , "is_edit": True})

@login_required
def delete(req, id):
    data = get_object_or_404(Inverntory, id=id)
    data.delete()
    return redirect('home')