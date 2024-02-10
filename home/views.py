from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# index page
def index(request):
    return render(request,'index.html')
# login page

def enter(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            print("invailid username and password")
            return redirect('/register/')
        else:
            login(request,user)
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
        gender=data.get('gender')
        state=data.get('state')
        zip=data.get('zipcode')
        dd=User.objects.filter(username=email)
        if dd.exists():
           print("email is already exists please try another email address")
           return redirect('/register/')
        
        dd=User.objects.create(
            username=email
        )
        dd.set_password(password)
        dd.save()
        user= registration.objects.create(
            full_name=full_name,
            fathers_name=father_name,
            email=email,
            gender=gender,
            state=state,
            code=password,
            address1=address1,
            address2=address2,
            city=city,
            zip=zip
        )
        subject="Email verification mail"
        message=" please click on the following link  :  http://127.0.0.1:8000/login/"
        from_email=settings.EMAIL_HOST_USER
        recipient_list=[email]
        send_mail(subject,message,from_email,recipient_list)
        return redirect("/page/")
        
    return render(request,'register.html')

# sample page

def sample(request):
    return render(request,'sample.html')


#  page


def page(request):
    return render(request,'page.html')