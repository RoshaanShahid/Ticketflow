import React, {useEffect, useState} from 'react';
import api from '../services/api';
import { useParams } from 'react-router-dom';

export default function TicketView(){
  const { id } = useParams();
  const [ticket, setTicket] = useState(null);
  useEffect(()=> {
    api.get(`tickets/${id}/`).then(res => setTicket(res.data)).catch(()=>{})
  },[id]);
  if (!ticket) return <div>Loading ticket...</div>;
  return (
    <div>
      <h3>Ticket {ticket.id}</h3>
      {ticket.qr_code ? <img src={ticket.qr_code} alt="QR" /> : <p>No QR yet</p>}
      <pre>{JSON.stringify(ticket, null, 2)}</pre>
    </div>
  )
}
