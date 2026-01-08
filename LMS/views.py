from django.shortcuts import render

# Create your views here.


def viewHome(request):
    resp = render(request, "LMS/home.html")
    return resp


def viewRegister(request):
    resp = render(request,"LMS/register.html")
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