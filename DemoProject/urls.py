"""
URL configuration for DemoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def viewSum(request,a,b):
    return HttpResponse("<h1>Hello I am calling SUM="+ str(a+b) +"</h1>")

def viewSub(request,a,b):
    return HttpResponse("<h1>Hello I am Calling Subtract="+str(a-b)+"</h1>")

def viewMult(request,a,b):
    return HttpResponse("<h1>Hello I am calling Multiplication="+str(a*b)+"</h1>")

def viewDivide(request,x,y):
    return HttpResponse("<h1>Hello I am calling Division= "+str(x/y)+"</h1>")


def viewHome(request):
    a = int(request.GET.get("t1",0))
    # print("----------------------",a)
    b = int(request.GET.get("t2",0))
    # print("--------------------",b)

    sum1 = a+b
    # print("Sum of the value is:",sum1)
    d1 = {'a':a,'b':b,'sum1':sum1}
    resp = render(request,"home.html", context=d1)
    return resp


def viewCalc(request):
    num1 = int(request.POST.get("t1",0))
    num2 = int(request.POST.get('t2',0))
    # print("-----t1-----------",num1,"----------t2---------",num2)
    if request.method == "GET":
        resp = render(request,"calculator.html")
        return resp
    elif 'btnsum' in request.POST:
        c = num1 + num2 
        # print(c)
    elif 'btnsub' in request.POST:
        c = num1-num2
    
    elif 'btnmult' in request.POST:
        c = num1*num2

    elif 'btndiv' in request.POST:
        c = num1/num2

    elif 'btnmod' in request.POST:
        c = num1%num2
        
    d1 = {"result":c, 'num1':num1, 'num2':num2}
    resp = render(request,"calculator.html",context=d1)
    return resp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:a>/<int:b>/',viewSum),
    path('sub/<int:a>/<int:b>/',viewSub),
    path('mult/<int:a>/<int:b>/',viewMult),
    path('divide/<int:x>/<int:y>/',viewDivide),
    path('home/',viewHome),  # http://127.0.0.1:8000/home/
    path("calc/",viewCalc),
    path('EMS/',include("EMS.urls")), # http://127.0.0.1:8000/EMS/
    path("SMS/",include("SMS.urls")), #http://127.0.0.1:8000/SMS/
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)