from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from LMS.decorator import is_CheckLoginorRegister
from django.contrib.auth.decorators import login_required


# Create your views here.


def viewHome(request):
    resp = render(request, "LMS/home.html")
    return resp

@is_CheckLoginorRegister
def viewRegister(request):
    if request.method  == "GET":
        frm_unbound = UserCreationForm() # empty form or without data
        d1 ={"form": frm_unbound}
        resp = render(request,"LMS/register.html",context=d1)
        return resp
    elif request.method == "POST":
        frm_bound = UserCreationForm(request.POST) # form with data
        if frm_bound.is_valid(): # validation 
            frm_bound.save()
            d1 = {"message":"User Registered Successfully!"}
            resp = render(request,"LMS/register.html",context=d1)
            return resp
        
        else:
            d1 = {"form":frm_bound}
            resp = render(request,"LMS/register.html",context=d1)
            return resp

@is_CheckLoginorRegister      
def viewLogin(request):
    if request.method == "GET":
        resp = render(request,"LMS/login.html")
        return resp
    elif request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        # print(username,password) it can display on console
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user) # create session
            # resp = HttpResponse("Login Successful")
            # return resp
            resp = render(request,"LMS/home.html")
            return resp
        else:
            resp = HttpResponse("Invalid Credentials")
            return resp


@login_required(login_url='login')  # to protect view
def viewSecure1(request):
    resp = render(request, "LMS/secure1.html")
    return resp


@login_required(login_url='login')  # to protect view
def viewSecure2(reqeust):
    resp = render(reqeust,"LMS/secure2.html")
    return resp


def viewUnsecure1(request):
    resp = render(request,"LMS/unsecure1.html")
    return resp



def viewUnsecure2(request):
    resp = render(request,"LMS/unsecure2.html")
    return resp

@login_required(login_url='login')  # to protect view
def viewLogout(request):
    logout(request=request) # destroy session
    resp = render(request,"LMS/home.html")
    return resp