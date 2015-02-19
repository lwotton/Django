from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tracker.models import Exercise, UserProfile, Activity
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

class ExerciseResource(ModelResource):
    class Meta:
        queryset = Exercise.objects.all()
        authorization= Authorization()
        resource_name = 'exercise'

class ActivityResource(ModelResource):

	user = fields.ForeignKey(UserResource, 'user')
	exercise = fields.ForeignKey(ExerciseResource, 'exercise')
    	class Meta:
        	queryset = Activity.objects.all()
        	resource_name = 'activity'
        	authorization = Authorization()
        	filtering = {
            'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        	}



