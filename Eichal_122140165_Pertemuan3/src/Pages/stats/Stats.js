import React from 'react';
import useBookStats from '../../hooks/UseBookStats';
import './Stats.css';

const Stats = () => {
  const { owned, reading, wishlist } = useBookStats();
  return (
    <div className="stats-page">
      <h1>Statistik Buku</h1>
      <p>Dimiliki: {owned}</p>
      <p>Sedang Dibaca: {reading}</p>
      <p>Ingin Dibeli: {wishlist}</p>
    </div>
  );
};

export default Stats;