import React from 'react';
import { useBooks } from '../../context/BookContext';
import './BookList.css';

const BookList = () => {
  const { filteredBooks, deleteBook } = useBooks();

  return (
    <ul className="book-list">
      {filteredBooks.map(book => (
        <li key={book.id} className="book-item">
          <strong>{book.title}</strong> oleh {book.author} ({book.status})
          <button onClick={() => deleteBook(book.id)}>Hapus</button>
        </li>
      ))}
    </ul>
  );
};

export default BookList;