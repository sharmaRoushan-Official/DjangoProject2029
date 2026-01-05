from SMS.models import Student 
from django import forms 


class StudentForm(forms.ModelForm): 
    class Meta:
        model = Student
        # fields = ['name','age']
        fields = '__all__'  # all fields from Student model
