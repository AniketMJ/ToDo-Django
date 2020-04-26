from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add'),
    path('delete/<int:pk>/', views.delete_todo, name='delete'),
    path('delete_completed/', views.delete_completed, name='delete_completed'),
    path('delete_selected/', views.delete_selected, name='delete_selected'),
    path('complete/<int:pk>', views.complete_todo, name='complete'),
    path('complete_all/', views.complete_all, name='complete_all'),
    path('complete_selected/', views.complete_selected, name='complete_selected'),
]
