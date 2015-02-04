from django.shortcuts import render
from django.views import generic
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from tracker.models import Exercise

class IndexView(generic.ListView):

	template_name = 'tracker/index.html'
	
	def get_queryset(self):
		return Exercise.objects.all


