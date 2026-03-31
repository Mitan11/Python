from django.shortcuts import render, redirect, get_object_or_404
from .models import Inverntory
from .forms import InventoryForm

# Create your views here.
def home(req):

    data = Inverntory.objects.all()

    return render(req, 'home.html' , {"data": data})

def add(req):
    if req.method == "POST":
        form = InventoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req , 'form.html' , {"form" : InventoryForm()})

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

def delete(req, id):
    data = get_object_or_404(Inverntory, id=id)
    data.delete()
    return redirect('home')