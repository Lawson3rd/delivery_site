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

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    return render(request, 'tracking/contact.html', {'form': form})

def track_shipment(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            shipment = Shipment.objects.get(tracking_number=tracking_number)
            return render(request, 'tracking/tracking_result.html', {'shipment': shipment})
        except Shipment.DoesNotExist:
            error = 'Tracking number not found.'
            return render(request, 'tracking/track.html', {
                'error': error,
                'form': TrackingForm()
            })
    return render(request, 'tracking/track.html', {'form': TrackingForm()})

def tracking_result(request):
    tracking_number = request.GET.get('tracking_number')
    shipment = get_object_or_404(Shipment, tracking_number=tracking_number)
    return render(request, 'tracking/tracking_result.html', {'shipment': shipment})
