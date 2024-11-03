# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    phone_number = forms.CharField(max_length=15, required=True, label="Número de Teléfono")
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), required=True, label="Fecha de Nacimiento")
    gender = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')], required=True, label="Sexo")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'birth_date', 'gender')


class AppointmentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    service = forms.CharField(max_length=200)  # Podrías usar un ChoiceField si tienes opciones fijas
    appointment_date = forms.DateField()
    appointment_time = forms.TimeField()
