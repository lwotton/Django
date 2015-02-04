from django.conf.urls import patterns, url

from tracker import views

urlpatterns = patterns('',
	# ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
   )