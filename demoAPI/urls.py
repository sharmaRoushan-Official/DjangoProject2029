from django.urls import path
from demoAPI.views import *

urlpatterns = [
    path('firstApi/', view_first_api, name='first-api'), # http://127.0.0.1:8000/demoapi/firstAPI/
    path('secondApi/', view_second_api, name='second-api'), # http://127.0.0.1:8000/demoapi/secondApi/
    path('trainers/', trainer_list, name='trainer-list'), # http://127.0.0.1:8000/demoapi/trainers/
    path('createTrainer/', create_trainer, name='create-trainer'), # http://127.0.0.1:8000/demoapi/createTrainer/
    path('updateTrainer/<int:id>/', update_trainer, name='update-trainer'), # http://127.0.0.1:8000/demoapi/updateTrainer/1/
    path('partialUpdateTrainer/<int:id>/', partial_update_trainer, name='partial-update-trainer'), # http://127.0.0.1:8000/demoapi/partialUpdateTrainer/1/
    path('deleteTrainer/<int:id>/', delete_trainer, name='delete-trainer'), # http://127.0.0.1:8000/demoapi/deleteTrainer/1/
    path('students/', student_list, name='student-list'), # http://127.0.0.1:8000/demoapi/students/
]
