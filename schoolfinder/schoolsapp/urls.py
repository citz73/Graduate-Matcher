"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import include, path
from schoolsapp import views 

urlpatterns = [
    path('', views.IndexView,name='index'),
    #path('<int:Location_id>/', views.IndexView.detail,name='detail'),
]

"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import include, path
from schoolsapp import views 

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:Location_id>/', views.detail,name='detail'),
]
