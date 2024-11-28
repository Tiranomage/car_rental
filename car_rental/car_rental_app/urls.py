from django.urls import path
from .views import CarListView, CarDetailView, BookingCreateView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/book/', BookingCreateView.as_view(), name='booking_create'),
]