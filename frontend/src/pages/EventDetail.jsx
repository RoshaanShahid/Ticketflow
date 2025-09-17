import React, {useEffect, useState} from 'react';
import api from '../services/api';
import SeatMap from '../components/SeatMap';
import { useParams, useNavigate } from 'react-router-dom';

export default function EventDetail(){
  const { id } = useParams();
  const [seats, setSeats] = useState([]);
  const [selected, setSelected] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    api.get(`events/${id}/seats/`).then(res => setSeats(res.data)).catch(()=>{});
  }, [id]);

  const onToggle = seatId => {
    setSelected(prev => prev.includes(seatId) ? prev.filter(s=>s!==seatId) : [...prev, seatId]);
  };

  const book = async () => {
    try {
      const res = await api.post('book/', { event_id: id, seat_ids: selected });
      // for now go to ticket viewer of first created ticket
      if (res.data.length) {
        const ticketId = res.data[0].id;
        navigate(`/tickets/${ticketId}`);
      }
    } catch (err){
      alert(err?.response?.data?.detail || 'Booking failed');
    }
  };

  return (
    <div>
      <h2>Event {id}</h2>
      <SeatMap seats={seats} selected={selected} onToggle={onToggle} />
      <button onClick={book} disabled={!selected.length}>Book {selected.length} seat(s)</button>
    </div>
  )
}
