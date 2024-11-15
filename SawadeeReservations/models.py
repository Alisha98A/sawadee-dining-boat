from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import timedelta, time

# Create your models here.
class Booking(models.Model):
    customer_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    booking_date = models.DateTimeField(blank=False, null=False)
    number_of_guests = models.PositiveIntegerField(default=4, validators=[MaxValueValidator(20), MinValueValidator(4)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.booking_date}"
