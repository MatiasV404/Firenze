from django.shortcuts import render,redirect

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
    return render(request, 'appointment.html')

def barbers(request):
    return render(request, 'barbers.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')