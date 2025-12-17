from django.urls import path
# from EMS.views import viewHome
from EMS.views import *



urlpatterns = [
    # path('home/',viewHome), # http://127.0.0.1:8000/EMS/home/
    # path('calc/',viewCalc), # http://127.0.0.1:8000/EMS/calc/
    # path('dtlFor/',viewHome2), # http://127.0.0.1:8000/EMS/dtlFor/
    # path('dummyEmp/',view_home), # http://127.0.0.1:8000/EMS/dummpyEmp/
    path('insertems/',view_insert_ems),
    path('customer/',viewCustomer, name='customer'),
    
]
