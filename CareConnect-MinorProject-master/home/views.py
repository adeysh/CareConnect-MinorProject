from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# index page
def index(request):
    data=profiledata.objects.all()
    return render(request,'index.html',context={'data':data})
# login page

def enter(request):
    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "Invalid username and password")
            return redirect('/login/')
        else:
            
            login(request,user)
            user=registration.objects.get(email=username)
            data=profiledata.objects.create(
                full_name=user.full_name,
                fathers_name=user.fathers_name,
                email=user.email,
                code=user.code,
                address1=user.address1,
                address2=user.address2,
                city=user.city,
                state=user.state,
                zip=user.zip

            )
            user.save()
            
            messages.success(request, "Login successfully")
        
            return render(request,'index.html',context={'user':user})
    
    return render(request,'Login.html')

# bedbooking page

def bedbooking(request):
    return render(request,'successfully.html')

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
        subject="Account Verification for CareConnect"
        message="Dear User,\n\n Thank you for registering with CareConnect.\n\n To complete the registration process and ensure the security of your account, please verify your email address by clicking the link below: \n http://127.0.0.1:8000/login/ \n\n If you are unable to click the link above, please copy and paste it into your web browser's address bar.\n\n Once your email address has been verified, you will gain full access to our platform and its features. \n\n If you did not register with CareConnect, please ignore this email.\n\n Thank you for choosing CareConnect. If you have any questions or need further assistance, please don't hesitate to contact us at CareConnect.support@gmail.com.\n\n Best regards"
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




# fillform page

def fillform(request,id):
    qq=beds.objects.get(id=id)
    nnn=profiledata.objects.all()
    if request.method=="POST":
        qq=beds.objects.get(id=id)
        data=request.POST
        hospital_name=data.get('Hospital_name')
        bed_id=data.get('Bed_id')
        room_number=data.get('Room_number')
        ward_number=data.get('Ward_number')
        disease=data.get('Disease')
        bed_type=data.get('Bed_type')
        pname=data.get('pname')
        page=data.get('page')
        pgender=data.get('pgender')
        address=data.get('address')
        mnumber=data.get('mnumber')
        emergancy=data.get('emergancy')
        currentmedications=data.get('currentmedications')
        allergies=data.get('allergies')
        pastsurgeries=data.get('pastsurgeries')
        insuranceprovider=data.get('insuranceprovider')
        policynumber=data.get('policynumber')
        specialrequests=data.get('specialrequests')
        user=patient_info.objects.create(
            Hospital_name=hospital_name,
            Bed_id=bed_id,
            Room_number=room_number,
            Ward_number=ward_number,
            Disease=disease,
            Bed_type=bed_type,
            patient_name=pname,
            patient_age=page,
            patient_gender=pgender,
            address=address,
            mobile_number=mnumber,
            current_medication=currentmedications,
            allergies=allergies,
            past_surgeries=pastsurgeries,
            insurance_policy=insuranceprovider,
            Policy_number=policynumber,
            special_request=specialrequests
        )
        user.save()
        qq.delete()
        return redirect('/bedbooking/')
    return render(request,'FillForm.html',context={'data':qq,'name':nnn})




# hospital's information
from django.db.models import Q

def hospitalinfo(request):
    data=info.objects.all()
    if request.GET.get('q'):
        search=request.GET.get('q')
        data=data.filter(
            Q(hospital_name__icontains=search)|
            Q(hospital_address__icontains=search)|
            Q(hospital_details__icontains=search)
        )
    return render(request,'name.html',context={'data':data})


def bedsinfo(request):
    data=beds.objects.all()
    if request.GET.get('q'):
        search=request.GET.get('q')
        data=data.filter(
            Q(Hospital_name__icontains=search)|
            Q(Bed_id__icontains=search)|
            Q(Room_number__icontains=search)|
            Q(Ward_number__icontains=search)|
            Q(Disease__icontains=search)|
            Q(Bed_type__icontains=search)
        )
    return render(request,'beds.html',context={'data':data})


def success(request):
    return render(request,'successfully.html')



def hospital(request):
    data=patient_info.objects.all()
    return render(request,'bedsdata.html',context={'data': data})


def delete_patient_data(request,id):
    data=patient_info.objects.get(id=id)
    qq=beds.objects.create(
        Hospital_name=data.Hospital_name,
        Room_number=data.Room_number,
        Ward_number=data.Ward_number,
        Bed_id=data.Bed_id,
        Bed_type=data.Bed_type,
        Disease=data.Disease
    )
    qq.save()
    data.delete()
    return redirect('/hospital/')

def search_patient(request):
    data=patient_info.objects.all()
    if request.GET.get('q'):
        search=request.GET.get('q')
        data=data.filter(
            Q(Hospital_name__icontains=search)|
            Q(Bed_id__icontains=search)|
            Q(Room_number__icontains=search)|
            Q(Ward_number__icontains=search)|
            Q(Disease__icontains=search)|
            Q(Bed_type__icontains=search)|
            Q(patient_name__icontains=search)|
            Q(patient_gender__icontains=search)|
            Q(patient_age__icontains=search)
        )
    return render(request,'bedsdata.html',context={'data':data})

def profile(request):
     if request.user.is_authenticated:
        return render(request,'profile.html')
     else:
         pass


def feedback(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        message=data.get('message')
        user=feed.objects.create(
            name=name,
            email=email,
            message=message
        )
        user.save()
        return redirect('/beds/')
    return render(request,'index.html')


def mainprofiledata(request):
    data=profiledata.objects.all()
    return render(request,'mainprofile.html',context={'data':data})

def removedata(request,id):
    
    user=profiledata.objects.get(id=id)
    user.delete()
    return redirect('/login/')