from django.contrib import admin
from .models import Deadline, Location, School, UserProfile



# Register your models here.
admin_models = [Deadline, Location, School, UserProfile]
admin.site.register(admin_models)