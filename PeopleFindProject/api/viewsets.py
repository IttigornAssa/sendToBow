from rest_framework import viewsets,mixins,filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProfilesSerialzer
from FindApp.models import Profiles
class ProfileViewset(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet
                    ):
    queryset            = Profiles.objects.all()
    serializer_class    = ProfilesSerialzer
    filter_backends     = (filters.SearchFilter,)
    # filter_fields       = ('name','last_name')
    search_fields       = ('name','last_name', 'position__jobdiscription__discription')