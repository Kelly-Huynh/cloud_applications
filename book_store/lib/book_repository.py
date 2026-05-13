from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author"], row["id"])
            books.append(item)
        return books
    
    def find(self, book_id):
        rows = self._connection.execute(
            'SELECT * FROM books WHERE id =%s', [book_id])
        row = row[0]
        return Book(row["id"], row["title"], row["author"])
    
    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author) VALUES (%s, %s)', 
            [book.title, book.author])
        return None
    
    def delete(self, book_id):
        self._connection.execute(
            'DELETE FROM books WHERE id = %s', [book_id])
        return None