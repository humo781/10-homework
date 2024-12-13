from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('list/', views.tasks_list, name='list'),
    path('detail/<int:pk>/', views.task_detail, name='detail'),
    path('create/', views.task_create, name='create'),
    path('update/<int:pk>/', views.task_update, name='update')
]
