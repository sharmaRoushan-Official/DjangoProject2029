from functools import wraps
from django.shortcuts import render

def is_CheckLoginorRegister(func): # decorator function (func)
    def inner(request): # wrapper function
        if request.user.is_authenticated: # check session
            return render(request,"LMS/home.html")  # redirect to home
        else:
            return func(request) # proceed to login or register
    return inner # decorator
