from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'appointment_date', 'created_at')
    list_filter = ('service', 'appointment_date')
    search_fields = ('name', 'phone')
    ordering = ('-created_at',)