from db_config import SessionLocal
from models import Book

# Sample book data
books_data = [
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "pages": 277},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 324},
    {"title": "1984", "author": "George Orwell", "pages": 328},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "pages": 279},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180},
    {"title": "Moby Dick", "author": "Herman Melville", "pages": 635},
    {"title": "War and Peace", "author": "Leo Tolstoy", "pages": 1225},
    {"title": "Ulysses", "author": "James Joyce", "pages": 730},
    {"title": "The Odyssey", "author": "Homer", "pages": 541},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "pages": 671},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "pages": 796},
    {"title": "Brave New World", "author": "Aldous Huxley", "pages": 268},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "pages": 158},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": 310},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "pages": 1178},
    {"title": "Jane Eyre", "author": "Charlotte Bronte", "pages": 507},
    {"title": "Wuthering Heights", "author": "Emily Bronte", "pages": 416},
    {"title": "Great Expectations", "author": "Charles Dickens", "pages": 505},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "pages": 864},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck", "pages": 464},
]

# Create a new database session
session = SessionLocal()

try:
    # Add each book to the database
    for book_data in books_data:
        book = Book(
            title=book_data["title"],
            author=book_data["author"],
            pages=book_data["pages"],
        )
        session.add(book)
    
    # Commit the transaction
    session.commit()
    print("20 books added successfully!")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    # Close the session
    session.close()
