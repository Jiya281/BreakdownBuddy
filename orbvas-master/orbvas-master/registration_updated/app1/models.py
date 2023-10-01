from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from app1.models import Mechanic


class Mechanic(models.Model):
    fullname = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=20)
    mail = models.EmailField()
    password = models.CharField(max_length=128, null=True)
    cpassword = models.CharField(max_length=128, null= True)
    address = models.TextField()
    exp = models.IntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.fullname
    
    # def __str__(self):
    #     return self.phoneno
    
    # def __str__(self):
    #     return self.mail
    
    # def __str__(self):
    #     return self.password
    
    # def __str__(self):
    #     return self.address
    
    # def __str__(self):
    #     return self.exp

# app1/models.py
# def my_function():
#     from app1.models import Mechanic
#     # Use the Mechanic model here

# def mechSignUp(request):
#     if request.method == 'POST':
#         uname= request.POST.get('fullname')
#         phone= request.POST.get('phoneno')
#         email= request.POST.get('mail')
#         password= request.POST.get('password')
#         cpassword= request.POST.get('confirmpass')
#         address= request.POST.get('address')
#         experience= request.POST.get('exp')
#         upload= request.POST.get('file')

#         mech= Mechanic.objects.create(fullname = uname, phoneno = phone, mail = email, password = password, address = address, exp = experience)

#         print(uname,phone,email,password,cpassword,address,experience,upload)
#     return render(request, 'mechSignUp.html')

# def mechLogin(request):
#     return render(request, 'mechLogin.html')