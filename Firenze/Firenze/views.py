from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .forms import AppointmentForm  # Asegúrate de que tienes un formulario creado
from django.views.decorators.csrf import csrf_exempt
from .forms import ExtendedUserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .productos import productos

from .models import Producto


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def appointment(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        # Aquí puedes agregar la lógica para enviar un correo
        try:
            send_mail(
                'Confirmación de cita',
                f'Hola {first_name} {last_name},\n\nHas reservado el servicio: {service} para el {date} a las {time}.\nNo lo olvides.\n\nSaludos,\nFirenze Spa',
                'cristiangaete32@gmail.com',  # Desde dónde se envía
                [email],  # A quién se envía
                fail_silently=False,
            )
            return HttpResponse("Cita solicitada con éxito.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            return HttpResponse("Error interno del servidor, no se pudo enviar el correo.", status=500)

    return render(request, 'appointment.html')


def barbers(request):
    return render(request, 'barbers.html', {'productos': productos})

def registro(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes redirigir o mostrar un mensaje de éxito
            return render(request, 'login.html')  # Cambia esto por tu redirección o mensaje de éxito
    else:
        form = ExtendedUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

def services(request):
    return render(request, 'services.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Cambia a la URL a la que deseas redirigir después del login
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')
    
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def productos_view(request):
    return render(request, 'productos.html', {'productos': productos})

def carrito(request):
    return render(request, 'carrito.html')