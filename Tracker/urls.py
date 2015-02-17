from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render

from tracker import views


urlpatterns = patterns('',
	# ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^users/', views.ListUserView.as_view(),
        name='users',),
    url(r'^activity/', views.activity, name='activity'),

   )