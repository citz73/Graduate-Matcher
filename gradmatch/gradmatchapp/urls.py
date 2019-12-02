from django.contrib import admin
from django.urls import path
from gradmatchapp import views


app_name = 'gradmatchapp'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:deadline_id>/', views.detail, name='detail'),
]