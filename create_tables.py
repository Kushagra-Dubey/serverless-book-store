from db_config import Base, engine
from models import Book  # Replace with the path to your model file

# Create all tables
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
