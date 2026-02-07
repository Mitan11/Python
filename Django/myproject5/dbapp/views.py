from django.shortcuts import render
from dbapp.models import Marks, Student

'''
# to get all data from database
data = Student.objects.all()

# to get specific data from database
data = Student.objects.get(roll=1)

# to insert data into database
student = Student.object.create(parameters)
'''

# Create your views here.
def home(req):
    
    return render(req , 'home.html')