from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render

from tracker import views
from tracker.views import Index

urlpatterns = patterns('',
	# ex: /polls/
    url(r'^users/', views.ListUserView.as_view(),
        name='users',),
    url(r'^$', Index.as_view(), name='index'),

   )