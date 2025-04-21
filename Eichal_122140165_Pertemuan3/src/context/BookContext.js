import React, { createContext, useContext, useState, useEffect } from 'react';
import useLocalStorage from '../hooks/UseLocalStorage';

const BookContext = createContext();

export const BookProvider = ({ children }) => {
  const [storedBooks, setStoredBooks] = useLocalStorage('books', []);
  const [books, setBooks] = useState(storedBooks);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState('');

  useEffect(() => {
    setStoredBooks(books);
  }, [books, setStoredBooks]);

  const addBook = (book) => {
    setBooks([...books, { ...book, id: Date.now() }]);
  };

  const updateBook = (id, updatedBook) => {
    setBooks(books.map(book => (book.id === id ? { ...book, ...updatedBook } : book)));
  };

  const deleteBook = (id) => {
    setBooks(books.filter(book => book.id !== id));
  };

  const filteredBooks = books.filter(book => {
    const matchesStatus = filterStatus ? book.status === filterStatus : true;
    const matchesSearch = book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          book.author.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesStatus && matchesSearch;
  });

  return (
    <BookContext.Provider value={{ books, addBook, updateBook, deleteBook, filteredBooks, setSearchTerm, setFilterStatus }}>
      {children}
    </BookContext.Provider>
  );
};

export const useBooks = () => useContext(BookContext);