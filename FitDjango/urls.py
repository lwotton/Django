from django.conf.urls import patterns, include, url
from django.contrib import admin
import registration
from tracker import views
from tracker.api import ExerciseResource, ActivityResource, UserResource
from django.views.generic import RedirectView

exercise_resource = ExerciseResource()
activity_resource = ActivityResource()
user_resource = UserResource()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/tracker/')),
    url(r'^tracker/', include('tracker.urls', namespace='tracker')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls', namespace='registration')),
    url(r'^api/', include(exercise_resource.urls)),
    url(r'^api/', include(activity_resource.urls)),
    url(r'^api/', include(user_resource.urls)),


)

