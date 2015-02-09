from tastypie.resources import ModelResource
from tracker.models import Exercise


class EntryResource(ModelResource):
    class Meta:
        queryset = Exercise.objects.all()
        resource_name = 'exercise'