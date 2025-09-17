from django.contrib import admin
from .models import Shipment, TrackingUpdate, ContactMessage  

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'status')
    search_fields = ('tracking_number', 'status', 'last_location')

@admin.register(TrackingUpdate)
class TrackingUpdateAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'status', 'location', 'timestamp')
    search_fields = ('status', 'location', 'shipment__tracking_number')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at') 
    ordering = ('-created_at',)  
