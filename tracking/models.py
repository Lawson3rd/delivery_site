from django.db import models

# Shipment Model
class Shipment(models.Model):
    STATUS_CHOICES = [
        ('Order Placed', 'Order Placed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]

    tracking_number = models.CharField(max_length=100, unique=True)
    receiver_name = models.CharField(max_length=100)
    sender_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    

    # ✅ dropdown status field
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    # ✅ automatically calculated stop position
    stop_position = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        """Auto update stop_position when saving shipment"""
        status_map = {
            'Order Placed': 0,
            'Out for Delivery': 1,
            'Delivered': 2,
        }
        self.stop_position = status_map.get(self.status, 0)
        super().save(*args, **kwargs)

    @property
    def progress_percent(self):
        """Convert stop_position to percentage (0–100%)"""
        return (self.stop_position / 4) * 200  # 4 steps total

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"


# Shipment Update Model (tracking timeline)
class TrackingUpdate(models.Model):
    shipment = models.ForeignKey(
        'Shipment', on_delete=models.CASCADE, related_name='updates'
    )
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.status} at {self.location} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"


# Contact Message Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
