from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

    def clean(self):
        # Ensure booking is within operational hours (10:00-22:00)
        if self.booking_date.time() < time(10, 0) or self.booking_date.time() >= time(22, 0):
            raise ValidationError("Bookings must be between 10:00 and 22:00.")

        # Check that number of guests is within the allowed range
        if not (4 <= self.number_of_guests <= 20):
            raise ValidationError("Number of guests must be between 4 and 20.")

 