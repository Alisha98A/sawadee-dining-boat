from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.BookingListView.as_view(), name='booking-list'),  # Booking list
    path('reservations/create/', views.BookingCreateView.as_view(), name='booking-create'),
    path('reservations/<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking-edit'),
    path('reservations/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking-delete'),
]