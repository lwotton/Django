from django.conf.urls import patterns, include, url
from django.contrib import admin
import registration
from tracker import views
from tracker.api import EntryResource
from django.views.generic import RedirectView

entry_resource = EntryResource()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/tracker/')),
    url(r'^tracker/', include('tracker.urls', namespace='tracker')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracker/accounts/', include('registration.urls', namespace='registration')),
    url(r'^tracker/api/', include(entry_resource.urls)),

)

