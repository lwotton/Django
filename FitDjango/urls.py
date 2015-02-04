from django.conf.urls import patterns, include, url
from django.contrib import admin
import registration
from tracker import views

urlpatterns = patterns('',
    url(r'^tracker/', include('tracker.urls', namespace='tracker')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls', namespace='registration')),

)