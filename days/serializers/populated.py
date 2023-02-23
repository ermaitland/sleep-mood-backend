from rest_framework import serializers
from ..models import Days
from sleep.serializers.common import MoodSerializer

class PopulatedDaysSerializer(serializers.ModelSerializer):
    mood = MoodSerializer