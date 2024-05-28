from django.urls import path
from  . import views

app_name = 'main'
urlpatterns = [
    path('', views.check_memory, name='check_memory'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path('check_memory/', views.check_memory, name='check_memory'),
    path('memory_form/', views.get_memory, name='memory_form'),
    path('edit_memory/<int:memory_id>/', views.edit_memory, name='edit_memory'),
]