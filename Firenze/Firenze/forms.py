from django import forms

class AppointmentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    service = forms.CharField(max_length=200)  # Podrías usar un ChoiceField si tienes opciones fijas
    appointment_date = forms.DateField()
    appointment_time = forms.TimeField()
