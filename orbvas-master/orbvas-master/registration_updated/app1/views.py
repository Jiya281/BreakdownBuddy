from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from app1.models import Mechanic
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect # Add this import
from django.db import models
from django.contrib.auth.hashers import make_password
# from django.views.decorators.csrf import login_required 
# Create your views here.

@csrf_protect  # Add the decorator here
# @login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

@csrf_protect  # Add the decorator here
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        phnno = request.POST.get('phnno')

        if pass1 != pass2:
            return HttpResponse("Your password does not match!!")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            
            my_user.save()
            return redirect('UserLogin')

        print(uname, email, pass1, pass2, phnno)
    return render(request, 'signup.html')

@csrf_protect  # Add the decorator here
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!!")

    return render(request, 'UserLogin.html')

# def view(request):
#     from app1.models import Mechanic

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
        
#         hashed_password = make_password(password)

#         mech= Mechanic.objects.create(fullname = uname, phoneno = phone, mail = email, password = password, address = address, exp = experience)
#         new_mechanic = Mechanic(uname='fullname', password='password')
#         new_mechanic.save()

#         mech.save()
#         return HttpResponse('User has been created')
#         print(uname,phone,email,password,cpassword,address,experience,upload)
#     return render(request, 'mechSignUp.html')
# from django.contrib.auth.hashers import make_password  # Import make_password



def mechSignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('fullname')
        phone = request.POST.get('phoneno')
        email = request.POST.get('mail')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirmpass')
        address = request.POST.get('address')
        experience = request.POST.get('exp')
        upload = request.POST.get('file')

        if password != cpassword:
            return HttpResponse('Passwords do not match')
        else:
            # Hash the password
            hashed_password = make_password(password)
            # Create and save the Mechanic object with the hashed password
            mech = Mechanic.objects.create(fullname=uname, phoneno=phone, mail=email, password=hashed_password, address=address, exp=experience)
            mech.save()

            # Redirect or return a success message
            return redirect('Mechaniclogin')     

    return render(request, 'mechSignUp.html')


def mechLogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!")

    return render(request, 'mechLogin.html')
