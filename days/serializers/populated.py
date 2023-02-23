from rest_framework import serializers
from ..models import Days
from sleep.serializers.common import MoodSerializer
from .common import DaysSerializer

class PopulatedDaysSerializer(DaysSerializer):
    mood = MoodSerializer()