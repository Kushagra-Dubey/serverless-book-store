# Google Cloud Pub/Sub + SQLAlchemy Project

## **Overview**
This project demonstrates how to integrate Google Cloud Pub/Sub with Python to process messages and connect to a PostgreSQL database using SQLAlchemy. The application sends messages to a Pub/Sub topic, processes them via a subscription trigger, and stores or retrieves data from a PostgreSQL database.

---

## **Features Implemented**
1. **Google Cloud Pub/Sub Integration**:
   - Send JSON messages to a Pub/Sub topic.
   - Automatically trigger a subscription to process incoming messages.
2. **PostgreSQL Database**:
   - Create a PostgreSQL database using Docker.
   - Connect to the database using SQLAlchemy.
   - Define and interact with database models.
3. **Python Scripting**:
   - Add data to the database using scripts.
   - Query and process data from the database.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8+
- Docker installed and running
- Google Cloud SDK installed and authenticated
- A Google Cloud project with Pub/Sub API enabled

---

### **2. Clone the Repository**
```bash
git clone <repository_url>
cd <repository_name>
```

---

### **3. Install Dependencies**
Create a virtual environment and install the required Python packages:
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate   # For Windows
pip install -r requirements.txt
```

---

### **4. Configure Environment Variables**
Create a `.env` file in the project root with the following content:
```plaintext
GOOGLE_APPLICATION_CREDENTIALS=service-account-key.json
PUBSUB_TOPIC=my-topic
PUBSUB_SUBSCRIPTION=my-subscription
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase
```

Ensure `service-account-key.json` is in the project directory.

---

### **5. Create a PostgreSQL Database Using Docker**
Run the following command to create a PostgreSQL container:
```bash
docker run --name postgres-container \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 -d postgres
```

---

### **6. Run the Application**
- **Send Messages to Pub/Sub**:
  ```bash
  python send.py
  ```
- **Process Messages Automatically**:
  Ensure the `process_subscription.py` script is running to handle incoming messages.
  ```bash
  python process_subscription.py
  ```
- **Add Books to PostgreSQL**:
  Use the `add_books.py` script to add 20 books to the database.
  ```bash
  python add_books.py
  ```

---

## **Files and Directories**
- **`send.py`**: Sends JSON messages to the Pub/Sub topic.
- **`process_subscription.py`**: Processes incoming messages automatically from the subscription.
- **`db_config.py`**: Configures SQLAlchemy connection to PostgreSQL.
- **`models.py`**: Defines database models.
- **`add_books.py`**: Adds 20 books to the PostgreSQL database.
- **`requirements.txt`**: Lists all Python dependencies.
- **`.env`**: Contains environment variables.

---

## **Sample JSON Message**
The following JSON message structure is used for Pub/Sub:
```json
{
  "Books": [
    {"book_id": 1, "book_name": "1984", "author_name": "George Orwell"},
    {"book_id": 2, "book_name": "The Great Gatsby", "author_name": "F. Scott Fitzgerald"}
  ],
  "Order_ID": "12345",
  "User_email": "user@example.com",
  "Address": {
    "city": "New York",
    "country": "USA",
    "pincode": "10001",
    "street_number": "5th Ave",
    "house_number": "101"
  }
}
```

---

## **Future Enhancements**
1. Implement API endpoints for interaction.
2. Add authentication for secure access.
3. Integrate additional Google Cloud services.

---

## **License**
This project is licensed under the MIT License.

