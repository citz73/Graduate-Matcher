from django.shortcuts import render
from django.http import HttpResponse
from .models import Deadline


# Create your views here.

def index(request):
    deadline_list = Deadline.objects.all()
    output = ','.join(deadline.name for deadline in deadline_list)
    return HttpResponse(output)


def detail(request):
    return HttpResponse("This is the detailed page")