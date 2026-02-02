from django.urls import path
from demoAPI.views import *

urlpatterns = [
    path('firstApi/', view_first_api, name='first-api'), # http://127.0.0.1:8000/demoapi/firstAPI/
    path('secondApi/', view_second_api, name='second-api'), # http://127.0.0.1:8000/demoapi/secondApi/
    path('trainers/', trainer_list, name='trainer-list'), # http://127.0.0.1:8000/demoapi/trainers/
]
