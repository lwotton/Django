from django.shortcuts import render
from django.views import generic
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from tracker.models import Exercise, UserProfile

class IndexView(generic.ListView):

    template_name = 'tracker/index.html'
    context_object_name = 'exercise_list'

    def get_queryset(self):
        return Exercise.objects.order_by('-pub_date')[:5]

class UserView(generic.ListView):
	template_name = 'tracker/users.html'
	context_object_name = 'users_list'

	def get_queryset(self):
		return Users.objects.all()


class ListUserView(generic.ListView):

    model = User
