from django.shortcuts import render
from django.views import generic
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from tracker.models import Exercise, UserProfile, Activity

class UserActivityView(generic.ListView):

	template_name='tracker/activity.html'	
	context_object_name = "users_activity"
	model = Activity

	def get_context_data(self,**kwargs):
		context = super(UserActivityView,self).get_context_data(**kwargs)
		context['activity_list'] = Activity.objects.all()
		return context


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

