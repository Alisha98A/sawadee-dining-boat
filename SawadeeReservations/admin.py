from django.contrib import admin
from .models import Booking
from django.utils import timezone

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone_number', 'booking_date', 'number_of_guests', 'created_on', 'updated_on')
    search_fields = ('customer_name', 'email', 'phone_number')
    list_filter = ('booking_date',)
    ordering = ('booking_date',)

admin.site.register(Booking, BookingAdmin)
