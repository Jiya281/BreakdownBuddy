# from django.contrib import admin
from django.contrib import admin
from .models import Mechanic

# admin.site.register(Mechanic)

# Register your models here.

class MechanicAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'password', 'phoneno', 'mail', 'address', 'exp')

admin.site.register(Mechanic, MechanicAdmin)
