from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foraged/', views.foraged, name='foraged'),
    path('forageDetail/<int:id>', views.forageDetail, name='detail'),
]