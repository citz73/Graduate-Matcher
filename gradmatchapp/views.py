from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Deadline, Location, School, User, UserProfile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import DeadlineForm


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
	user_list = School.objects.filter(userprofile__user = request.user)
	return render(request, "gradmatchapp/profile.html", {'user_list': user_list})  
  	
def listUserCredential(request):
	if request.user.is_authenticated:
		user_deadline = Deadline.objects.filter(userprofile__user = request.user)
		if User.objects.filter(userprofile__user = request.user).exists():	
			user_info = User.objects.get(userprofile__user = request.user)
		else:
			user_info = None

		if UserProfile.objects.filter(user = request.user).exists():
			user_credential = UserProfile.objects.get(user = request.user)
		else:
			user_credential = None	
	else:
		user_deadline = None
		user_info = None
		user_credential = None
	context = {'user_deadline': user_deadline, 'user_info': user_info, 'user_credential': user_credential}
	return render(request, "gradmatchapp/index.html", context)


def add_deadline(request):
	submitted = False
	if request.method == 'POST':
		form = DeadlineForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_deadline/?submitted=True')
	else:
		form = DeadlineForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'gradmatchapp/add_deadline.html', {'form': form, 'submitted': submitted})

	# safe check