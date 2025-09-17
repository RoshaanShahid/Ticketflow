from rest_framework import serializers
from .models import Seat, Ticket
from events.serializers import EventSerializer

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id','row','number','seat_type','price','is_booked']

class TicketSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Ticket
        fields = ['id','event','seat','user','created_at','status','qr_code']
