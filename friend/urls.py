from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foraged/', views.foraged, name='foraged'),
    path('forageDetail/<int:id>', views.forageDetail, name='detail'),
    path('newforaged/', views.newForaged, name='newforaged'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]