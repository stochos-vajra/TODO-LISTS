from django.urls import path



from .views import *

 
urlpatterns = [

    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('random/', random_task, name='random_task'),
]
