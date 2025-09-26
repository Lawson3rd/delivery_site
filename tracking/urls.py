from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/', views.track_shipment, name='track_shipment'),  # renamed for clarity
    path('tracking/<str:tracking_number>/', views.tracking_result, name='tracking_result'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('track/', views.track, name='track'),
    path('tracking/<str:tracking_number>/', views.tracking_result, name='tracking_result'),
]
