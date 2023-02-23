from rest_framework import serializers
from ..models import Days

class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = '__all__'