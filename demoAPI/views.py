from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from demoAPI.models import Trainer
from demoAPI.serializers import TrainerSerializer
from rest_framework import status

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
# GET - Fetching the data
# many=True - when we are fetching multiple records
# many=False - when we are fetching single record
# return Response (serializer.data) - it returns the serialized data as JSON response

# Post - Creating new record

@api_view(http_method_names=['POST'])
def create_trainer(request):
    serializer = TrainerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)  # HTTP 201 Created
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  # HTTP 400 Bad Request

# request.data =- JSON input data from the client
# is_valid() - validates the input data against the model fields
# save() - saves the new record to the database


# PUT - Update Full object 

@api_view(http_method_names=['PUT'])
def update_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    serializer = TrainerSerializer(trainer,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

# PUT - Updates all fields of the existing record
# missing field - error 
# Used for complete replacement


# PATCH - Update Partial object


@api_view(http_method_names=['PATCH'])
def partial_update_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    serializer = TrainerSerializer(trainer,data=request.data,partial=True) # key difference is here
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# PATCH - Updates only specified fields of the existing record
# partial = True -> allows missing fields 
# Most used in real projects 

@api_view(http_method_names=['DELETE'])
def delete_trainer(request,id):
    triner = Trainer.objects.get(id=id)
    triner.delete()
    return Response(status = status.HTTP_204_NO_CONTENT) # HTTP 204 No Content

# Deletes record permanently from the database
# No data is returned in the response


    

