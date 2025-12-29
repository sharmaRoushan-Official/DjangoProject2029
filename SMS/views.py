from django.shortcuts import render
from SMS.models import *
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


def viewPayment(request):

    pay = PaymentDetails.objects.all()
    stu = Student.objects.all()
    cou = Course.objects.all()
    d1 = {'payment':pay,'students':stu,'course':cou}
    if request.method == "POST":

        pass
    return render(request,"SMS/createPayment.html",context=d1)
    

