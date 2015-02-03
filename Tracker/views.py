from django.shortcuts import render
from django.views import generic

from tracker.models import Exercise

class IndexView(generic.ListView):

	template_name = 'tracker/index.html'
	
	def get_queryset(self):
		return Exercise.objects.all
