from django.contrib import admin
from django.urls import path, include
from gradmatchapp import views


app_name = 'gradmatchapp'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('<int:deadline_id>/', views.DetailView.as_view(), name='detail'),
    path('locations', views.LocationsView.as_view(), name='locations'),
    path('locations/<slug:pk>', views.LocationView.as_view(), name='location'),
    path('locations/<slug:pk>/<int:school_id>', views.SchoolDetail.as_view(), name='schoolview'),
    path('signup', views.SignUpView.as_view(), name= 'signup'),
    path('profile', views.listUserSchool, name = 'profile'),
    
]