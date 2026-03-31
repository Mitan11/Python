from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(req):
    return render(req , 'home.html')

def login(req):
    form = UserLoginForm()

    if req.method == 'POST':
        form = UserLoginForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:
                auth_login(req, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")

    return render(req, 'login.html', {'form': form})

def logout(req):
    auth_logout(req)
    return redirect('login')