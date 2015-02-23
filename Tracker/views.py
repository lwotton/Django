from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tracker.models import Exercise, UserProfile, Activity

class Index(View):

	def get(self,request):
	
		if request.user.is_authenticated():
			latest_activity = Activity.objects.filter(user__username=request.user.username)

			context = {'latest_activity': latest_activity}
	
		else:
    			latest_activity = Activity.objects.all()
    
    			context = {'latest_activity': latest_activity}
    	
    		return render(request, 'tracker/index.html', context)


class UserView(generic.ListView):
	template_name = 'tracker/users.html'
	context_object_name = 'users_list'

	def get_queryset(self):
		return Users.objects.all()

class Profile(View):
	def get(self,request):

			user_details = UserProfile.objects.all()
			
			context = {'user_details':user_details}

			return render(request, 'tracker/profile.html', context)



class ListUserView(generic.ListView):

    model = User

