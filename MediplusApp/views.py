from django.shortcuts import render
from MediplusApp.models import contact,bookAppointment,Department
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorator import is_checkloginorRegister


# Create your views here.


def view_Home(request):
    resp = render(request,"MediplusApp/home.html")
    return resp


def view_About(request):
    resp = render(request,'MediplusApp/about.html')
    return resp

def view_Doctors(request):
    resp = render(request,"MediplusApp/doctor.html")
    return resp

def view_Contact(request):
    if request.method == "GET":
        resp = render(request,"MediplusApp/contact.html")
        return resp
    elif request.method == "POST":
        if 'btnsubmit' in request.POST:
            con = contact()
            con.name = request.POST.get("name","NA")
            con.email = request.POST.get("email","NA")
            con.phone_no = request.POST.get("phone","NA")
            con.subject = request.POST.get("subject","NA")
            con.message = request.POST.get("message","NA")
            con.save()
            resp = render(request,"MediplusApp/contact_success.html")
            return resp
        else:
            pass


def view_Services(request):
    resp = render(request,"MediplusApp/services.html")
    return resp

def view_404(request):
    resp = render(request,"MediplusApp/404.html")
    return resp

def view_appointment(request):
    resp = render(request,"MediplusApp/appointment.html")
    return resp

@is_checkloginorRegister
def view_login(request):
    if request.method  == "GET":
        resp = render(request,'MediplusApp/login.html')
        return resp
    elif request.method =="POST":
        u_name = request.POST.get("username","NA")
        u_password=request.POST.get("password","NA")
        user = authenticate(request,username=u_name,password=u_password)
        if user is not None:
            login(request,user)
            # resp = HttpResponse("<h1>Login Successfully!!</h1>")
            # return resp
            resp = render(request,"MediplusApp/login_success.html")
            return resp
        else:
            # resp = HttpResponse("<h1>Login Failed!</h1>")
            # return resp 
            resp = render(request,"LMS/login.html")
            return resp
        
@login_required(login_url='login')
def view_logout(request):
    logout(request=request)
    resp= render(request,"MediplusApp/logout.html")
    return resp

def view_register(request):
    resp = render(request, 'MediplusApp/register.html')
    return resp


def bookAppointment(request):
    if request.method == "GET":
        department = Department()
        d1 ={'department':department}
        print('--------------------',d1)
        resp = render(request,'MediplusApp/home.html',context=d1)
        return resp
    elif request.method == 'POST':
        if 'btn' in request.POST:
            appointment=bookAppointment()
            appointment.name = request.POST.get("Uname","NA")
            appointment.email = request.POST.get("Uemail","NA")
            appointment.phone_no = request.POST.get("Uphone","NA")
            appointment.department = request.POST.get("Udepartment","NA")
            appointment.doctors_name = request.POST.get("Udoctor","NA")
            appointment.date = request.POST.get("Udate","NA")
            appointment.message=request.POST.get("Umessage","NA")
            appointment.save()
            resp = HttpResponse("<h1>Appointment Booked!! Doctor will be meet you soon!!</h1>")
            return resp
        else:
            resp = HttpResponse("<h1> Data Not Submitted!! Failed</h1>")
            return resp
    else:
        pass
        

