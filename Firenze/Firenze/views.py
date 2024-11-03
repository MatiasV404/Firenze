from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .forms import AppointmentForm  # Asegúrate de que tienes un formulario creado
from django.views.decorators.csrf import csrf_exempt




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
    return render(request, 'barbers.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')