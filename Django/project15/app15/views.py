from django.shortcuts import render,redirect,get_object_or_404
from .models import student 
from .forms import studentForm,loginForm,UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(req):
    data=student.objects.all()
    return render(req,"home.html",{"data":data})


# delete
@login_required
def delete(req,id):
    data=get_object_or_404(student,id=id)
    data.delete()
    return redirect('home')


# add
@login_required
def add(req):
    form = studentForm()
    
    if req.method == 'POST':
        form = studentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(req,'form.html',{"form":form})

# edit

@login_required
def edit(req,id):
    data=get_object_or_404(student,id=id)
    form = studentForm(instance=data)
    if req.method == 'POST':
        form = studentForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(req,'form.html',{"form":form})



# login

def loginUser(req):
    form=loginForm()
    if req.method == 'POST':
        form = loginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(req,username=username , password=password)

            if user:
                login(req , user)
                return redirect('home')

    return render(req,"login.html",{"form":form})




# logout
def logoutUser(req):
    logout(req)
    return redirect('login')

# register
def register(req):
    form = UserRegistrationForm()
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home')

    return render(req , 'register.html' , {'form' : form})