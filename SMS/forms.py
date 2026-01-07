from SMS.models import Student,CourseStudent,PaymentDetails
from django import forms 

# student registration form
class StudentForm(forms.ModelForm):  # model form
    class Meta:
        model = Student 
        fields = '__all__'  # all fields from Student model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = 'Enter ' + field.label
            



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



