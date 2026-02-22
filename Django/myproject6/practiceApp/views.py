from django.shortcuts import render

'''
python manage.py shell

from myapp.models import MyModel

Create:variableName =  MyModel.objects.create(field=value)
Query: variableName = MyModel.objects.filter(field=value)
Update: obj.field = new_value; obj.save()
Delete: obj.delete()
'''

'''
# to get all data from database
data = Student.objects.all()

# to get specific data from database
data = Student.objects.get(roll=1)

# to insert data into database
student = Student.object.create(parameters)

# to update data into database
student = Student.objects.get(roll=1)
student.name = "new name"
student.save()

# to delete data from database
student = Student.objects.get(roll=1)
student.delete()
student.save()
'''

# Create your views here.
def home(req):
    return render(req , "practiceApp/home.html")

def about(req):
    return render(req , "practiceApp/about.html")