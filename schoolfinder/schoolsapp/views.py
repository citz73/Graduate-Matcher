'''
from django.shortcuts import render
from django.views import generic
from .models import Location
#Create your views here.

class IndexView(generic.ListView):
    template_name = 'schoolsapp/index.html'

    def get_queryset(self):
        return Location.objects.all()
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
from django.template import loader


# Create your views here.

def index(request):
    school_list = Location.objects.all()
    template = loader.get_template('schoolsapp/index.html')
    context = {
        'school_list': school_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, school_id):
    return HttpResponse("This is school number {}".format(school_id))
