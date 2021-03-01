from rest_framework import serializers

from blood_group.models import Location, Doner

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')

class DonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doner
        fields = ('__all__')