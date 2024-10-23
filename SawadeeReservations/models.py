from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    booking_date = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.booking_date}"
