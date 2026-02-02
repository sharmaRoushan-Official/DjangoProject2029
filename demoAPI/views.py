from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from demoAPI.models import Trainer
from demoAPI.serializers import TrainerSerializer

# Create your views here.


# @api_view(['GET']) # second method 

@ api_view(http_method_names=['GET']) # first method    
def view_first_api(request): # first API view
    resp = Response({"data":"This is my first API response using DRF"}) # It returns JSON response
    return resp

@api_view(http_method_names=['GET','POST'])
def view_second_api(request): # second API view
    resp = Response({"data":"congratulations! You have created your second API using DRF"})
    return resp

@api_view(http_method_names=['GET'])
def trainer_list(request):
    if request.method == "GET":
        trainers = Trainer.objects.all()
        # print("Trainders:",trainers)
        serializer = TrainerSerializer(trainers,many=True)
        return Response(serializer.data)
    

