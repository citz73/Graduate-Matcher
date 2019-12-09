from django import forms
from django.forms import ModelForm
from .models import Deadline


class DeadlineForm(ModelForm):
	required_css_class = 'required'
	class Meta:
		model = Deadline
		fields = '__all__'