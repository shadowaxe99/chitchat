```python
import sqlite3
from sqlite3 import Error
from datetime import datetime

DATABASE = "chatbot_assistant.db"

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)
    return conn

def logUserInput(user_input, bot_response):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO ChatHistorySchema(user_input, bot_response, timestamp) VALUES(?,?,?)", (user_input, bot_response, timestamp))
        conn.commit()

def get_chat_history():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM ChatHistorySchema")
        rows = cur.fetchall()
        return rows
```