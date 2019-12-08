from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Deadline, Location, School, User
from django.shortcuts import render
# from rest_framework import filters
# from rest_framework.permissions import 	IsAuthenticated


class IndexView(generic.ListView):
	template_name = 'gradmatchapp/index.html'

	def get_queryset(self):
		return Deadline.objects.all()


class LocationsView(generic.ListView):
	template_name = 'gradmatchapp/locations.html'

	def get_queryset(self):
		return Location.objects.all()


class LocationView(generic.DetailView):
	model = Location
	template_name = 'gradmatchapp/locationview.html'


class SchoolDetail(generic.DetailView):
	model = School
	template_name = 'gradmatchapp/schoolview.html'


class DetailView(generic.DetailView):
	model = Deadline
	template_name = 'gradmatchapp/detailview.html'

class SignUpView(generic.CreateView):
		form_class = UserCreationForm
		success_url = reverse_lazy('gradmatchapp:login')
		template_name = 'gradmatchapp/signup.html'

def listUserSchool(request):
	user_list = School.objects.filter(user = request.user)
	return render(request, "gradmatchapp/profile.html", {'user_list': user_list})  

# class UserView(generic.ListView):
#     user = request.user

# 	model = School
# 	template_name = 'gradmatchapp/profile.html'
  	

