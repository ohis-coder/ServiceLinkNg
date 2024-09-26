from django.db import models

class ServiceProvider(models.Model):
    SERVICE_CHOICES = [
        ('plumber', 'Plumber'),
        ('barber', 'Barber'),
        ('mechanic', 'Mechanic'),
        ('laundry', 'Laundry'),
        ('tutor', 'Tutor'),
        ('trade', 'Goods Exchange')
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    description = models.TextField(blank=True, default="No description")
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    location = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    #service_type = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} - {self.service_type}"
    




