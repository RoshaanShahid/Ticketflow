from django.db import transaction
from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core import signing
from .models import Seat, Ticket
from .serializers import SeatSerializer, TicketSerializer
from .utils import generate_ticket_qr
from users.permissions import IsOrganizer

class EventSeatsAPIView(generics.ListAPIView):
    serializer_class = SeatSerializer
    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Seat.objects.filter(event_id=event_id).order_by('row','number')

class BookSeatsAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        event_id = request.data.get('event_id')
        seat_ids = request.data.get('seat_ids', [])
        user = request.user
        if not seat_ids or not event_id:
            return Response({'detail':'event_id and seat_ids required'}, status=400)
        with transaction.atomic():
            seats = list(Seat.objects.select_for_update().filter(id__in=seat_ids, event_id=event_id))
            if len(seats) != len(seat_ids):
                return Response({'detail':'Some seats not found'}, status=400)
            for seat in seats:
                if seat.is_booked:
                    return Response({'detail':f'Seat {seat.row}{seat.number} already booked'}, status=400)
            tickets = []
            for seat in seats:
                seat.is_booked = True
                seat.save()
                t = Ticket.objects.create(event_id=event_id, seat=seat, user=user, status='paid')  # set paid for MVP
                generate_ticket_qr(t)
                tickets.append(t)
        serializer = TicketSerializer(tickets, many=True, context={'request': request})
        return Response(serializer.data, status=201)

from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOrganizer])
def validate_ticket(request, signed_payload):
    try:
        data = signing.loads(signed_payload)
    except signing.BadSignature:
        return Response({'valid': False, 'reason': 'bad_signature'}, status=400)
    ticket_id = data.get('ticket_id')
    ticket = Ticket.objects.filter(id=ticket_id).first()
    if not ticket:
        return Response({'valid': False}, status=404)
    if ticket.status == 'used':
        return Response({'valid': False, 'reason': 'already_used'}, status=400)
    ticket.status = 'used'
    ticket.save()
    return Response({'valid': True, 'ticket_id': str(ticket.id)})
