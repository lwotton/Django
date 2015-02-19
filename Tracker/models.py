from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save

class UserProfile(models.Model):

	user = models.OneToOneField(User)
	age = models.IntegerField(default=0)
	location = models.CharField(max_length=50, default=0)
	sex = models.CharField(max_length=10, default=0) 
	def __str__(self):
		return str(self.user)

class Exercise(models.Model):

	exercise = models.CharField(max_length=200)

	def __str__(self):
		return self.exercise

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class Activity(models.Model):
	
	user = models.ForeignKey(User)
	exercise = models.ForeignKey(Exercise)
	date = models.DateTimeField('date done')
	weight = models.IntegerField(max_length=10, default=0)
	reps = models.IntegerField(max_length=3, default=0)
	def __str__(self):
		return str(self.user)

post_save.connect(create_user_profile, sender=User)
