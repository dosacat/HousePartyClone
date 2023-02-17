from rest_framework import serializers
from .models import Room

# Serializers in Django REST Framework are responsible for 
# converting objects into data types understandable by 
# javascript and front-end frameworks.

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')