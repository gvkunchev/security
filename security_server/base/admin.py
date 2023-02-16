from django.contrib import admin
from .models import Sensor


class SensorAdmin(admin.ModelAdmin):
    list_display = ('location', 'state')


admin.site.register(Sensor, SensorAdmin)
