from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *

# index page
def index(request):
    return render(request,'index.html')
# login page

def enter(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=lo.objects.create(
            username=username
        )
        return redirect('/index/')
    
    return render(request,'Login.html')

# bedbooking page

def bedbooking(request):
    return render(request,'bedBooking.html')

# Fillform page

def fillform(request):
    return render(request,'FillForm.html')

# register page

def register(request):
    if request.method=="POST":
        data=request.POST
        full_name=data.get('fullname')
        father_name=data.get('fathersname')
        email=data.get('email')
        password=data.get('password')
        address1=data.get('address1')
        address2=data.get('address2')
        city=data.get('city')
        zip=data.get('zipcode')
        user= registration.objects.create(
            full_name=full_name,
            fathers_name=father_name,
            email=email,
            password=password,
            address1=address1,
            address2=address2,
            city=city,
            zip=zip
        )
        user.save()
        
    return render(request,'register.html')

# sample page

def sample(request):
    return render(request,'sample.html')
