from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.


def view_student_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        mobileNo = request.POST.get('mobileNo')
        dob = request.POST.get("dob")
        pic = request.FILES.get('pic')

        Student.objects.create(
            name = name,
            age = age,
            mobileNo = mobileNo,
            dob = dob, 
            pic = pic
        )
        return HttpResponse("<h1>Data Inserted Successfully!!</h1>")
    
    return render(request,"SMS/studentReg.html")
    

