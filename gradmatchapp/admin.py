from django.contrib import admin
from .models import Deadline, Location, School


# Register your models here.
admin_models = [Deadline, Location, School]
admin.site.register(admin_models)