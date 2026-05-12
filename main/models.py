from django.db import models

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('ultrasound', 'Ultrasound'),
        ('xray', 'X-Ray'),
        ('pregnancy', 'Pregnancy Scan'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name