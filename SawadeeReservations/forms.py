from django import forms
from .models import Booking
from datetime import time, datetime
from django.utils import timezone

# Define available time slots
TIME_SLOTS = [
    (time(hour, 0), f"{hour:02}:00 - {hour + 2:02}:00")
    for hour in range(10, 22, 2)
]

# Define available guest options
GUEST_OPTIONS = [(i, i) for i in range(4, 21)]  # Options from 4 to 20

class BookingAdminForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        label="Booking Date",
        initial=timezone.now().date(),  # Set initial value to today
    )
    booking_time = forms.TimeField(
        widget=forms.Select(choices=TIME_SLOTS),
        label="Time Slot",
    )
    number_of_guests = forms.ChoiceField(
        choices=GUEST_OPTIONS,
        label="Number of Guests",
    )

    class Meta:
        model = Booking
        fields = '__all__'

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get("booking_date")
        if booking_date and booking_date < timezone.now().date():
            raise forms.ValidationError("You cannot book for a date in the past.")
        return booking_date

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get("booking_time")
        booking_date = self.cleaned_data.get("booking_date")

        if booking_date:
            # Check if booking is for today
            if booking_date == timezone.now().date():
                current_time = timezone.now().time()
                if booking_time < current_time:
                    raise forms.ValidationError("This time slot has already passed for today.")
        return booking_time

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("booking_date")
        time_slot = cleaned_data.get("booking_time")

        if date and time_slot:
            # Combine date and time to form a datetime object for booking_date
            cleaned_data["booking_date"] = datetime.combine(date, time_slot)
        return cleaned_data