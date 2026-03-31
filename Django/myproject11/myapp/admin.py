from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name" , "age" , "email" , "date_of_join")

admin.site.register(Employee , EmployeeAdmin)