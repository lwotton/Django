from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save

class UserProfile(models.Model):

	user = models.ForeignKey(User, unique=True)
	
	def __str__(self):
		return str(self.user)

class Exercise(models.Model):

	person = models.ForeignKey(UserProfile)
	exercise = models.CharField(max_length=200)
	reps = models.IntegerField(default=0)
	date = models.DateTimeField('date done')
	
	def __str__(self):
		return self.exercise

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
