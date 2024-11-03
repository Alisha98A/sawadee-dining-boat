from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta, time

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

        # Ensure booking duration is exactly 2 hours
        end_time = self.booking_date + timedelta(hours=2)
        if end_time.time() > time(22, 0):
            raise ValidationError("Booking end time exceeds operating hours.")

        # Check for overlapping bookings (2-hour slot uniqueness)
        overlapping_bookings = Booking.objects.filter(
            booking_date__lt=end_time,
            booking_date__gte=self.booking_date
        ).exclude(id=self.id)
        if overlapping_bookings.exists():
            raise ValidationError("The selected time slot is already booked.")

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving
        super().save(*args, **kwargs)
