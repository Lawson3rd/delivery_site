from django.db import models

# Shipment Model
class Shipment(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    last_location = models.CharField(max_length=100, blank=True, null=True)
    estimated_delivery = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number

# Shipment Update Model
class TrackingUpdate(models.Model):
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, related_name='updates')
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.status} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# ✅ Contact Message Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
