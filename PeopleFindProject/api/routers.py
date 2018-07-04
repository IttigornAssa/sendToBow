from rest_framework import routers
from .viewsets import ProfileViewset
router = routers.DefaultRouter()
router.register(r'profile',ProfileViewset) 