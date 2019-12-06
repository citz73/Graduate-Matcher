from django.views import generic
from .models import Deadline, Location, School
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

# class UserView(generic.DetailView):
    
# 	model = 
# 	template_name = 'gradmatchapp/'
