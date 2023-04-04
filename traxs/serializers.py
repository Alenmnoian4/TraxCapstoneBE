from .models import Trax
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TraxSerializer
class TraxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Trax
        # the fields that should be included in the serialized output
        fields = ['id', 'name', 'workout', 'meal', 'weight', 'notes']