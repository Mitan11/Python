from django.contrib import admin
from .models import student

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=('name','roll_no','subject')

admin.site.register(student,studentadmin)    