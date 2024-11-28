from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Car, Booking
from .forms import BookingForm

class CarListView(ListView):
    model = Car
    template_name = 'car_rental_app/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_rental_app/car_detail.html'
    context_object_name = 'car'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'car_rental_app/booking_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.car = Car.objects.get(pk=self.kwargs['pk'])
        form.instance.total_price = ((form.instance.end_date - form.instance.start_date).days + 1) * form.instance.car.price_per_day
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.kwargs['pk']})