import os
import json
from google.cloud import pubsub_v1
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch values from the .env file
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
SUBSCRIPTION_NAME = os.getenv("SUBSCRIPTION_NAME")

def process_message(message_data):
    """
    Process the incoming message (e.g., print or manipulate it).
    """
    try:
        # Parse the message data from JSON
        message_json = json.loads(message_data)
        
        # Process the message (for example, print out the details)
        print(f"Received message for order id: {message_json['order_id']}")
        
        # Acknowledge the message
        return True
    except Exception as e:
        print(f"Error processing message: {e}")
        return False

def callback(message):
    """
    Callback function that is called when a message is received.
    """
    print(f"Received message: {message.data.decode('utf-8')}")
    
    # Process the message
    if process_message(message.data):
        message.ack()  # Acknowledge that the message was successfully processed
        print("Message acknowledged.")
    else:
        message.nack()  # If there was an error, we can nack the message
        print("Message failed to process. Will try again.")

def receive_messages():
    """
    Continuously receives messages from the subscription.
    """
    # Set the environment variable for authentication
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME)

    # Subscribe to the subscription
    print(f"Listening for messages on {subscription_path}...")
    
    # The subscribe method will call the callback function whenever a new message is received
    subscriber.subscribe(subscription_path, callback=callback)

    # Keep the main thread alive to listen for messages
    while True:
        pass

if __name__ == "__main__":
    receive_messages()
