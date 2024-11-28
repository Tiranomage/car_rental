from django import forms
from .models import Booking

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': CustomDateInput(format='%d.%m.%Y'),
            'end_date': CustomDateInput(format='%d.%m.%Y'),
        }