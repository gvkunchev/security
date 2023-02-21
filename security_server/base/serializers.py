from rest_framework import serializers
from .models import Sensor, ArmStatus


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('location', 'state')


class ArmStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArmStatus
        fields = ('location', 'state')
