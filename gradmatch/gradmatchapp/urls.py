from django.contrib import admin
from django.urls import path
from gradmatchapp import views


app_name = 'gradmatchapp'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:deadline_id>/', views.DetailView.as_view(), name='detail'),
    path('schools', views.SchoolView.as_view(), name='schoolview'),
]