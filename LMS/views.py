from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.


def viewHome(request):
    resp = render(request, "LMS/home.html")
    return resp


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


def viewSecure1(request):
    resp = render(request, "LMS/secure1.html")
    return resp


def viewSecure2(reqeust):
    resp = render(reqeust,"LMS/secure2.html")
    return resp


def viewUnsecure1(request):
    resp = render(request,"LMS/unsecure1.html")
    return resp



def viewUnsecure2(request):
    resp = render(request,"LMS/unsecure2.html")
    return resp