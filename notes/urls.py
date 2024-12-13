from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('list/', views.notes_list, name='list'),
    path('detail/<int:pk>/', views.note_detail, name='detail'),
    path('create/', views.note_create, name='create'),
    path('update/<int:pk>/', views.note_update, name='update')
]
