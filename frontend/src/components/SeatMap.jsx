import React from 'react';

export default function SeatMap({ seats, selected, onToggle }) {
  // convert seat list into rows -> arrays
  const grid = {};
  let rows = [];
  seats.forEach(s => {
    grid[s.row] = grid[s.row] || [];
    grid[s.row].push(s);
    if (!rows.includes(s.row)) rows.push(s.row);
  });
  rows.sort();
  return (
    <div>
      {rows.map(row => (
        <div key={row} style={{display:'flex', gap:8, marginBottom:8}}>
          <div style={{width:30}}><strong>{row}</strong></div>
          <div style={{display:'flex', gap:8}}>
            {grid[row].sort((a,b)=>a.number-b.number).map(seat => {
              const sel = selected.includes(seat.id);
              return (
                <button
                  key={seat.id}
                  disabled={seat.is_booked}
                  onClick={() => onToggle(seat.id)}
                  style={{
                    padding:8,
                    borderRadius:6,
                    border: sel ? '2px solid #0b84ff' : '1px solid #ccc',
                    background: seat.is_booked ? '#ddd' : 'white',
                    cursor: seat.is_booked ? 'not-allowed' : 'pointer'
                  }}
                >
                  {seat.number}
                </button>
              )
            })}
          </div>
        </div>
      ))}
    </div>
  )
}
