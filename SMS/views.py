from django.shortcuts import render,redirect
from SMS.models import *
from django.http import HttpResponse
from SMS.forms import StudentForm,CourseStudentForm,PaymentDetailsForm

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
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":
        amount = request.POST.get("amount")
        payment_mode = request.POST.get("payment_mode")
        student_id = request.POST.get("student")

        PaymentDetails.objects.create(
            amount=amount,
            payment_mode=payment_mode,
            student_id=student_id
        )

        return render(request,"SMS/paymentSuccess.html")  
    

    context = {
        'students': students,
        'courses': courses
    }
    return render(request, "SMS/createPayment.html", context)
    


def view_student_frm(request):
    if request.method == "GET":
        frm_unbound = StudentForm() # unbound  = no data
        context = {
            'frm': frm_unbound
        }
        return render(request, "SMS/studentForm.html", context)
    elif request.method == "POST":
        # frm_bound = StudentForm(request.POST) # bound form = with data
        frm_bound = StudentForm(request.POST, request.FILES) # bound form = with data
        if frm_bound.is_valid():
            frm_bound.save()
            resp = HttpResponse("<h1>Student Data Saved Successfully!!</h1>")
            return resp
    else:
        context = {
            'frm': frm_bound   
        }
        return render(request, "SMS/studentForm.html", context)
    
def view_course_student_frm(request):
    if request.method == "GET":
        frm_unbound = CourseStudentForm() # unbound  = no data
        context = {
            'frm': frm_unbound
        }
        return render(request, "SMS/courseStudentForm.html", context)
    elif request.method == "POST":
        frm_bound = CourseStudentForm(request.POST) # bound form = with data
        if frm_bound.is_valid():
            frm_bound.save()
            resp = HttpResponse("<h1>Course-Student Data Saved Successfully!!</h1>")
            return resp
    else:
        context = {
            'frm': frm_bound   
        }
        return render(request, "SMS/courseStudentForm.html", context)
    

def viewPaymentDetailsfrm(request):
    if request.method == "GET":
        frm_unbound = PaymentDetailsForm() # unbound  = no data
        context = {
            'frm': frm_unbound
        }
        return render(request, "SMS/paymentDetailsForm.html", context)
    elif request.method == "POST":
        frm_bound = PaymentDetailsForm(request.POST) # bound form = with data
        if frm_bound.is_valid():
            frm_bound.save()
            resp = HttpResponse("<h1>Payment Details Saved Successfully!!</h1>")
            return resp
    else:
        context = {
            'frm': frm_bound   
        }
        return render(request, "SMS/paymentDetailsForm.html", context)
    


def view_staticFile_Ex(request):
    resp = render(request, "SMS/staticFileExample.html")
    return resp