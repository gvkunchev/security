from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.serializers import StatusSerializer
from base.models import Sensor


@api_view(['GET',])
def get_sensor_status(request):
    """Return list of all sensors."""
    serializer = StatusSerializer(Sensor.objects.all(), many=True)
    return Response(serializer.data)
