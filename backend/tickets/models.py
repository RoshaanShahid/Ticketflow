import uuid
from django.db import models
from django.conf import settings

class Seat(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=4)
    number = models.IntegerField()
    seat_type = models.CharField(max_length=50, default='standard')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_booked = models.BooleanField(default=False)  # or use status field

    class Meta:
        unique_together = ('event','row','number')

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('reserved','reserved'),('paid','paid'),('used','used')], default='reserved')
    qr_code = models.ImageField(upload_to='qrcodes/', null=True, blank=True)
