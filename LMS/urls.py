from django.urls import path
from LMS.views import *



urlpatterns = [
    path("home/",viewHome,name="home"),
    path("register/",viewRegister,name="register"),
    path("secure1/",viewSecure1,name='secure1'),
    path("secure2/",viewSecure2,name='secure2'),
    path("unsecure1/",viewUnsecure1,name="unsecure1"),
    path("unsecure2/",viewUnsecure2,name='unsecure2'),
]
