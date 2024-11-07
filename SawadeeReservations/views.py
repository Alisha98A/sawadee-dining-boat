from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def menu(request):
    return render(request, 'menu.html')


# List View for bookings
class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        # Show only upcoming bookings starting from today's date
        return Booking.objects.filter(booking_date__gte=timezone.now()).order_by('booking_date')

# Create View for new bookings
class BookingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['customer_name', 'email', 'phone_number', 'booking_date', 'number_of_guests']
    
    def get_success_url(self):
        return reverse_lazy('booking-list')

# Update View for editing existing bookings
class BookingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['customer_name', 'email', 'phone_number', 'booking_date', 'number_of_guests']
    
    def get_success_url(self):
        return reverse_lazy('booking-list')

# Delete View for deleting bookings
class BookingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking-list')