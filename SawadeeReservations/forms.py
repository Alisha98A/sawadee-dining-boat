from django import forms
from .models import Booking
from datetime import time, datetime
from django.utils import timezone
from .models import Booking

class Meta:
        model = Booking
        fields = '__all__'
