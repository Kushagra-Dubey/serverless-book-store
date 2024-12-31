# Google Cloud Pub/Sub Project with Python

This project demonstrates the use of **Google Cloud Pub/Sub** with Python to implement a simple messaging system. Messages are published to a Pub/Sub topic and automatically processed when received by a subscription. The system follows good software development practices, including environment variable management and a structured Python environment.

---

## Features

1. **Publish Messages**:
   - Send JSON messages to a Pub/Sub topic using `send.py`.
   - Messages include structured data like books, user details, and address.

2. **Subscribe and Process Messages**:
   - A Python script (`receive_and_process.py`) listens for new messages on the subscription.
   - Automatically triggers a callback function to process the incoming messages.

3. **Environment Variables**:
   - Sensitive data and configurations are managed securely using a `.env` file.

4. **Service Account Integration**:
   - Authenticates with Google Cloud using a Service Account JSON key file.

---

## Prerequisites

### Google Cloud Setup

1. **Create a Pub/Sub Topic**:
   - Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new Pub/Sub topic.

2. **Create a Subscription**:
   - Attach a subscription to the Pub/Sub topic created.

3. **Create a Service Account**:
   - Go to the IAM & Admin section.
   - Create a Service Account with the `Pub/Sub Admin` role.
   - Download the JSON key file.

4. **Enable Pub/Sub API**:
   - Ensure the Pub/Sub API is enabled for your project.

### Local Setup

1. **Install Python**:
   - Ensure Python 3.8+ is installed.

2. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

3. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory:
     ```plaintext
     GOOGLE_APPLICATION_CREDENTIALS=./service-account-key.json
     PROJECT_ID=your-project-id
     TOPIC_NAME=your-topic-name
     SUBSCRIPTION_NAME=your-subscription-name
     ```
   - Replace placeholders with your actual values.

---

## Usage

### 1. Publish a Message

Run the `send.py` script to publish a message to the topic:

```bash
python send.py
```

This script sends a JSON message with the following structure:

```json
{
  "Books": [
    {"book_id": 1, "book_name": "Book One", "author_name": "Author A"},
    {"book_id": 2, "book_name": "Book Two", "author_name": "Author B"}
  ],
  "Order_ID": "12345",
  "User_email": "user@example.com",
  "Address": {
    "city": "CityName",
    "country": "CountryName",
    "pincode": "123456",
    "street_number": "10",
    "house_number": "20"
  }
}
```

### 2. Listen for Messages and Process Them

Run the `receive_and_process.py` script to listen for incoming messages:

```bash
python receive_and_process.py
```

- The script listens to the subscription and triggers the callback function whenever a new message is received.
- The message is processed, and its contents are printed.

---

## Code Structure

```
project-directory/
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
├── send.py                      # Script to publish messages to the topic
├── receive_and_process.py       # Script to listen for messages and process them
├── service-account-key.json     # Google Cloud Service Account key (secure this file)
```

---

## Additional Notes

1. **Error Handling**:
   - The callback function (`callback`) in `receive_and_process.py` gracefully handles errors during message processing.
   - Messages that fail to process are "nacked" and will be retried by Pub/Sub.

2. **Acknowledgement**:
   - Messages are acknowledged (`message.ack()`) only after successful processing to avoid duplication.

3. **Keep Subscriber Running**:
   - The `receive_and_process.py` script runs indefinitely to continuously listen for new messages.

---

## Requirements

- Python 3.8+
- Google Cloud SDK (optional for local testing)

### Dependencies

The `requirements.txt` file contains:

```plaintext
google-cloud-pubsub
python-dotenv
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Future Enhancements

1. **Deploy Subscriber to Google Cloud Functions**:
   - Move the subscriber logic to a cloud function for better scalability and reliability.

2. **Add Logging**:
   - Implement structured logging to monitor message processing.

3. **Testing**:
   - Add unit tests to ensure robust message handling.

4. **Extend Message Processing**:
   - Integrate with databases or APIs for more complex workflows.

---

## License

This project is licensed under the MIT License.

