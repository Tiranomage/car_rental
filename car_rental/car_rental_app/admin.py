from django.contrib import admin
from django.forms import DateInput
from .models import Car, Booking

class CustomDateInput(DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'total_price')
    list_filter = ('start_date', 'end_date')
    search_fields = ('user__username', 'car__brand', 'car__model')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['start_date', 'end_date']:
            kwargs['widget'] = CustomDateInput(format='%d.%m.%Y')
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Car)
admin.site.register(Booking, BookingAdmin)