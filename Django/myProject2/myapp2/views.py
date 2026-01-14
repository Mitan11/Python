from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request , 'myapp2/index.html')

def BecomeAPartner(request):
    return render(request , 'myapp2/becomeAPartner.html')

def ContactUs(request):
    return render(request , 'myapp2/contact.html')

def BecomeASupplier(request):
    return render(request , 'myapp2/becomeASupplier.html')