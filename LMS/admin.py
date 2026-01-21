from django.contrib import admin
from EMS.models import Customer,Employee
from SMS.models import *

# Register your models here.


@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['name','age',"address","mobileNo","salary"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age',"mobileno","address"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'mobileNo', 'dob', 'created_date', 'last_modified_date']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course']


@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['amount', 'payment_mode', 'payment_date', 'student']
