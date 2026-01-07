from django.urls import path
from SMS.views import *


urlpatterns = [
    path('stuReg/',view_student_registration), # http://127.0.0.1:8000/SMS/stuReg/
    path('createPay/',viewPayment,name="viewPayment"),
    path('stuFrm/',view_student_frm,name="view_student_frm"),
    path('courseStuFrm/',view_course_student_frm,name="view_course_student_frm"),
    path('payDetailsFrm/',viewPaymentDetailsfrm,name="view_payment_details_frm"),
    path('staticEx/',view_staticFile_Ex,name="view_static_file_ex"),
]
