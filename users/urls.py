from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.show_user, name='user'),
    path('register/', views.register, name='register'),
    path('delete-user/<int:id>', views.delete_user, name='delete-user'),
    path('update-user/<int:id>', views.update_user, name='update-user'),
    path('change-password', views.Change_password, name='change-password'),
    path('reset-password/<int:id>', views.Reset_password, name='reset-password')
]