
from django.contrib import admin
from tracker.models import Exercise,UserProfile,Activity
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Activity

class ChoiceInline(admin.TabularInline):
	model = UserProfile

class ChoiceInline(admin.TabularInline):
	model = Exercise

admin.site.register(Activity)
admin.site.register(Exercise)
admin.site.register(UserProfile)
