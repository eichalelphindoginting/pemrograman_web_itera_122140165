import React from 'react';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';
import { useBooks } from '../../context/BookContext';
import './Home.css';

const Home = () => {
  const { addBook } = useBooks();
  return (
    <div className="home-page">
      <h1>Manajemen Buku</h1>
      <BookForm onSubmit={addBook} />
      <BookFilter />
      <BookList />
    </div>
  );
};

export default Home;
