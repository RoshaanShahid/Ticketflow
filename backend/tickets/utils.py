import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.core import signing
from django.conf import settings

def generate_ticket_qr(ticket):
    payload = signing.dumps({'ticket_id': str(ticket.id)})
    # point to validation endpoint (dev). For production use full domain
    url = f"http://localhost:8000/api/tickets/validate/{payload}/"
    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    ticket.qr_code.save(f"{ticket.id}.png", ContentFile(buffer.getvalue()))
    ticket.save()
