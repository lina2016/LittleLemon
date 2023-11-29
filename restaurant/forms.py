from django import forms
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})
        }