import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './BookForm.css';

const BookForm = ({ onSubmit, initialData }) => {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('milik');
  const [error, setError] = useState('');

  useEffect(() => {
    if (initialData) {
      setTitle(initialData.title);
      setAuthor(initialData.author);
      setStatus(initialData.status);
    }
  }, [initialData]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title || !author) {
      setError('Judul dan penulis wajib diisi');
      return;
    }
    setError('');
    onSubmit({ title, author, status });
    setTitle('');
    setAuthor('');
    setStatus('milik');
  };

  return (
    <form className="book-form" onSubmit={handleSubmit}>
      {error && <p className="error">{error}</p>}
      <input placeholder="Judul" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Penulis" value={author} onChange={(e) => setAuthor(e.target.value)} />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="milik">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
      <button type="submit">Simpan</button>
    </form>
  );
};

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  initialData: PropTypes.object,
};

export default BookForm;