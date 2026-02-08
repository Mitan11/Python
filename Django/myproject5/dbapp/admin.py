# Python manage.py makemigrations 
# Python manage.py migrate

from django.contrib import admin
from .models import Student , Marks
# Register your models here.

# admin.site.register(Student)
# or
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id" ,'roll', 'name' , 'phone', 'course', 'totalMarks', 'percentage']

admin.site.register(Student, StudentAdmin)

class MarksAdmin(admin.ModelAdmin):
    list_display = ["id" ,'studentRoll', 'cn', 'dbms', 'python', 'aiml']

admin.site.register(Marks, MarksAdmin)