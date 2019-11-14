from django.shortcuts import render
from django.http import HttpResponse
from .models import Deadline
from django.template import loader


# Create your views here.

def index(request):
    deadline_list = Deadline.objects.all()
    template = loader.get_template('gradmatchapp/index.html')
    context = {
        'deadline_list': deadline_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, deadline_id):
    return HttpResponse("This is deadline number {}".format(deadline_id))