from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TrackingForm, ContactForm
from .models import Shipment, ContactMessage


def home(request):
    fact_labels = ['Happy Clients', 'Projects', 'Team Members', 'Awards']
    return render(request, 'tracking/home.html', {
        'now': now(),
        'fact_labels': fact_labels,
    })


def about(request):
    return render(request, 'tracking/about.html')


def services(request):
    return render(request, 'tracking/services.html')


def track(request):
    """Simple page with tracking form"""
    return render(request, 'tracking/track.html', {'form': TrackingForm()})


def contact(request):
    """Contact form handler"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'tracking/contact.html', {'form': form})


def track_shipment(request):
    """Handles tracking form submission"""
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            shipment = Shipment.objects.get(tracking_number=tracking_number)

            # ✅ Use progress_percent field from model
            shipment.progress_width = f"{shipment.progress_percent}%"

            return render(request, 'tracking/tracking_result.html', {'shipment': shipment})
        except Shipment.DoesNotExist:
            error = 'Tracking number not found.'
            return render(request, 'tracking/track.html', {
                'error': error,
                'form': TrackingForm()
            })
    return render(request, 'tracking/track.html', {'form': TrackingForm()})


def tracking_result(request, tracking_number):
    """Direct tracking URL: /tracking/<tracking_number>/"""
    shipment = get_object_or_404(Shipment, tracking_number=tracking_number)

    # ✅ Use progress_percent field from model
    shipment.progress_width = f"{shipment.progress_percent}%"

    return render(request, 'tracking/tracking_result.html', {'shipment': shipment})
