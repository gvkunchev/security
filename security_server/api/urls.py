from django.urls import path

from . import views


urlpatterns = [
    path('get_sensor_status', views.get_sensor_status),
    path('get_arm_status', views.get_arm_status),
    path('arm', views.arm),
    path('unarm', views.unarm),
    path('verify', views.verify)
]