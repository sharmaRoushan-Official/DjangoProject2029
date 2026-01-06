from SMS.models import Student,CourseStudent,PaymentDetails
from django import forms 

# student registration form
class StudentForm(forms.ModelForm):  # model form
    class Meta: # meta data
        model = Student # which model to use
        # fields = ['name','age']
        fields = '__all__'  # all fields from Student model

# course student form
class CourseStudentForm(forms.ModelForm):
    class Meta:
        model = CourseStudent
        fields = '__all__'

# payment details form
class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model = PaymentDetails
        fields = '__all__'



