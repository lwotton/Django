from django.contrib import admin

from django.contrib import admin
from tracker.models import Exercise,UserProfile
# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Exercise
	extra = 3

class ProfileAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,		{'fields':['user']}),
	]
	inlines = [ChoiceInline]
	search_fields = ['user']

admin.site.register(UserProfile, ProfileAdmin)
