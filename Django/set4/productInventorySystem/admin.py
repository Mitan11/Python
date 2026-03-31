from django.contrib import admin
from .models import Inverntory

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category')

admin.site.register(Inverntory, InventoryAdmin)
