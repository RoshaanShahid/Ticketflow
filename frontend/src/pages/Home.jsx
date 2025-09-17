import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Link } from 'react-router-dom';

export default function Home(){
  const [events, setEvents] = useState([]);
  useEffect(()=> {
    api.get('events/').then(res => setEvents(res.data)).catch(()=>{})
  }, []);
  return (
    <div>
      <h1>Events</h1>
      <ul>
        {events.map(e => <li key={e.id}><Link to={`/events/${e.id}`}>{e.title}</Link></li>)}
      </ul>
    </div>
  )
}
