import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';
import './App.css';

const App = () => {
  return (
    <BookProvider>
      <Router>
        <nav className="navbar">
          <Link to="/">Home</Link>
          <Link to="/stats">Statistik</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </Router>
    </BookProvider>
  );
};

export default App;
