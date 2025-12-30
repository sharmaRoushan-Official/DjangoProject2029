from django.urls import path
from SMS.views import *


urlpatterns = [
    path('stuReg/',view_student_registration), # http://127.0.0.1:8000/SMS/stuReg/
    path('createPay/',viewPayment,name="viewPayment"),
    
]
