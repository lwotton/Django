from django.conf.urls import patterns, include, url
from django.contrib import admin
import registration
from tracker import views
from tracker.api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('',
    url(r'^tracker/', include('tracker.urls', namespace='tracker')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls', namespace='registration')),
    url(r'^api/', include(entry_resource.urls)),

)