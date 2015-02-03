from django.db import models

class Exercise(models.Model):

	exercise_name = models.CharField(max_length=200)