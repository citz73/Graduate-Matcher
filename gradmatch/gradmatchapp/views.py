from django.views import generic
from .models import Deadline, Location


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
	template_name = 'gradmatchapp/location.html'


class DetailView(generic.DetailView):
	model = Deadline
	template_name = 'gradmatchapp/detail.html'
