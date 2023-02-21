from django.contrib import admin
from .models import Sensor, ArmStatus


class SensorAdmin(admin.ModelAdmin):
    list_display = ('location', 'state')

class ArmStatusAdmin(admin.ModelAdmin):
    list_display = ('location', 'state')


admin.site.register(Sensor, SensorAdmin)
admin.site.register(ArmStatus, ArmStatusAdmin)
