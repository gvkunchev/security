from rest_framework import serializers
from .models import Sensor


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('location', 'state')
