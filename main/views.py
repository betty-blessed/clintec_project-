from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
import urllib.parse
from django.shortcuts import render
from django.utils import timezone
from .models import Appointment
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/login/')
def dashboard(request):
    total = Appointment.objects.count()
    recent = Appointment.objects.order_by('-created_at')[:5]

    return render(request, 'main/dashboard.html', {
        'total': total,
        'recent': recent
    })

def dashboard(request):
    total_appointments = Appointment.objects.count()

    today = timezone.now().date()
    today_appointments = Appointment.objects.filter(appointment_date=today).count()

    upcoming_appointments = Appointment.objects.filter(
        appointment_date__gt=today
    ).count()

    recent_appointments = Appointment.objects.order_by('-created_at')[:5]

    context = {
        'total_appointments': total_appointments,
        'today_appointments': today_appointments,
        'upcoming_appointments': upcoming_appointments,
        'recent_appointments': recent_appointments,
    }

    return render(request, 'main/dashboard.html', context)


def home(request):
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'main/home.html', {'form': form})




def book(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save()

            # Build WhatsApp message
            message = (
                f"Hello Clintec, I have booked an appointment.\n"
                f"Name: {appointment.name}\n"
                f"Phone: {appointment.phone}\n"
                f"Service: {appointment.service}\n"
                f"Date: {appointment.appointment_date}"
            )

            encoded_message = urllib.parse.quote(message)

            whatsapp_url = f"https://wa.me/254708300588?text={encoded_message}"

            messages.success(request, "Booking successful! Redirecting to WhatsApp...")

            return redirect(whatsapp_url)

    else:
        form = AppointmentForm()

    return render(request, 'main/book.html', {'form': form})

def services(request):
    return render(request, 'main/services.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
def ultrasound(request):
    return render(request, 'main/ultrasound.html')

def xray(request):
    return render(request, 'main/xray.html')

