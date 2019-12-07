from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Deadline, Location, School, User
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

class UserView(generic.ListView):
    	model = User
    	template_name = 'gradmatchapp/profile.html'



# class UserView(generic.DetailView):
    
# 	model = 
# 	template_name = 'gradmatchapp/'
