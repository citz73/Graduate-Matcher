from django.views import generic
from .models import Deadline, Location


class IndexView(generic.ListView):
	template_name = 'gradmatchapp/index.html'

	def get_queryset(self):
		return Deadline.objects.all()


class SchoolsView(generic.ListView):
	template_name = 'gradmatchapp/schools.html'

	def get_queryset(self):
		return Location.objects.all()


class DetailView(generic.DetailView):
	model = Deadline
	template_name = 'gradmatchapp/detail.html'
