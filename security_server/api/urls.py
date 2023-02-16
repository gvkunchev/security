from django.urls import path

from . import views


urlpatterns = [
    path('get_sensor_status', views.get_sensor_status)
]