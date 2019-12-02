from django.shortcuts import render
from django.http import HttpResponse
from .models import Deadline
from django.template import loader


# Create your views here.

def index(request):
    deadline_list = Deadline.objects.all()

    context = {
        'deadline_list': deadline_list
    }
    return render(request, 'gradmatchapp/index.html', context)


def detail(request, deadline_id):
	# get the deadline, pk is primary key
	deadline = Deadline.objects.get(pk=deadline_id)
	context = {
		'deadline': deadline,
	}
	return render(request, 'gradmatchapp/detail.html', context)