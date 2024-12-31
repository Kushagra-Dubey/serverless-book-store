import os
import json
from google.cloud import pubsub_v1
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch values from the .env file
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
TOPIC_NAME = os.getenv("TOPIC_NAME")

def publish_message(topic_name, message):
    """
    Publishes a message to the Pub/Sub topic.
    """
    # Set the environment variable for authentication
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, topic_name)
    
    try:
        # Convert the dictionary to JSON string and encode it to bytes
        message_json = json.dumps(message).encode('utf-8')
        
        # Publish the message
        future = publisher.publish(topic_path, message_json)
        print(f"Message published: {message}")
        print(f"Message ID: {future.result()}")
    except Exception as e:
        print(f"Failed to publish message: {e}")

def create_message():
    """
    Creates a sample message with books, order ID, user email, and address.
    """
    # Sample JSON message
    message = {
        "books": [
            {
                "book_id": 1,
                "book_name": "The Great Gatsby",
                "author_name": "F. Scott Fitzgerald"
            },
            {
                "book_id": 2,
                "book_name": "1984",
                "author_name": "George Orwell"
            }
        ],
        "order_id": "123456789",
        "user_email": "user@example.com",
        "address": {
            "city": "New York",
            "country": "USA",
            "pincode": "10001",
            "street_number": "12",
            "house_number": "34"
        }
    }
    
    return message

if __name__ == "__main__":
    message = create_message()
    publish_message(TOPIC_NAME, message)
