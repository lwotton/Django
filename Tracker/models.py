from django.db import models
import datetime
from django.utils import timezone

class Exercise(models.Model):

	exercise_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.exercise_name
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Reps(models.Model):

	exercise= models.ForeignKey(Exercise)
	weight = models.CharField(max_length=200)
	reps = models.IntegerField(default=0)
	
	def __str__(self):
		return self.weight