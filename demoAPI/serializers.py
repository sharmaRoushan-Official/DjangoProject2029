from rest_framework import serializers
from demoAPI.models import Trainer

from SMS.models import Student

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


# ModelSerializer: Automatically creates serializer fields based on the model fields
# Meta: configuration to serialize 
# model: which model to serialize
# fields: '__all__'  Include all fields of the model Trainer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"




