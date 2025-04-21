import React from 'react';
import { useBooks } from '../../context/BookContext';
import './BookFilter.css';

const BookFilter = () => {
  const { setSearchTerm, setFilterStatus } = useBooks();

  return (
    <div className="book-filter">
      <input placeholder="Cari buku..." onChange={(e) => setSearchTerm(e.target.value)} />
      <select onChange={(e) => setFilterStatus(e.target.value)}>
        <option value="">Semua</option>
        <option value="milik">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
    </div>
  );
};

export default BookFilter;