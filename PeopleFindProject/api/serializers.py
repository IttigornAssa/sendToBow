from rest_framework import serializers
from FindApp.models import Profiles

class ProfilesSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'