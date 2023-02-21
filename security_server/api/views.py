import logging
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.serializers import StatusSerializer, ArmStatusSerializer
from base.models import Sensor, ArmStatus


logger = logging.getLogger('default_logger')


@api_view(['GET',])
def get_sensor_status(request):
    """Return list of all sensors."""
    serializer = StatusSerializer(Sensor.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET',])
def get_arm_status(request):
    """Return arm status."""
    serializer = ArmStatusSerializer(ArmStatus.objects.all().first())
    return Response(serializer.data)

@api_view(['GET',])
def arm(request):
    """Set to arm status."""
    arm_status = ArmStatus.objects.all().first()
    if arm_status.state == ArmStatus.Status.UNARMED:
        arm_status.state = ArmStatus.Status.ARMED
        logger.info('Setting arm status.')
    arm_status.save()
    serializer = ArmStatusSerializer(arm_status)
    return Response(serializer.data)

@api_view(['GET',])
def unarm(request):
    """Set to unarm status."""
    arm_status = ArmStatus.objects.all().first()
    arm_status.state = ArmStatus.Status.UNARMED
    logger.info('Setting unarm status.')
    arm_status.save()
    serializer = ArmStatusSerializer(arm_status)
    return Response(serializer.data)

@api_view(['GET',])
def verify(request):
    """Verify unlock pattern."""
    try:
        pattern = request.GET.get('pattern')
        if pattern != os.environ.get('UNLOCK_PATTERN'):
            logger.warning(f'Incorrect pattern detected: {pattern}')
            raise Exception('Incorrect pattern')
    except:
        return Response({'result': 'NOK'})
    return Response({'result': 'OK'})
