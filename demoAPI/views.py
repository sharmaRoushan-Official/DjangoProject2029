from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


# @api_view(['GET']) # second method 

@ api_view(http_method_names=['GET']) # first method    
def view_first_api(request):
    resp = Response({"data":"This is my first API response using DRF"})
    return resp

