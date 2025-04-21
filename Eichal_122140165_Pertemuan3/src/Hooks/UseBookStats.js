import { useBooks } from '../context/BookContext';

const useBookStats = () => {
  const { books } = useBooks();

  const owned = books.filter(book => book.status === 'milik').length;
  const reading = books.filter(book => book.status === 'baca').length;
  const wishlist = books.filter(book => book.status === 'beli').length;

  return { owned, reading, wishlist };
};

export default useBookStats;