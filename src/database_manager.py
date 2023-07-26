```python
import sqlite3
from sqlite3 import Error

DATABASE = "chatbot_assistant.db"

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE)
        print(f"SQLite connection with {DATABASE} established.")
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    try:
        conn.close()
        print(f"SQLite connection with {DATABASE} closed.")
    except Error as e:
        print(e)

def manageDatabase():
    conn = create_connection()
    if conn is not None:
        # create user preferences table
        create_table(conn, UserPreferencesSchema)
        # create task table
        create_table(conn, TaskSchema)
        # create chat history table
        create_table(conn, ChatHistorySchema)
    else:
        print("Error! cannot create the database connection.")
    close_connection(conn)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

UserPreferencesSchema = """ CREATE TABLE IF NOT EXISTS user_preferences (
                                        id integer PRIMARY KEY,
                                        response_time text NOT NULL,
                                        task_categorization text NOT NULL,
                                        notification_preferences text NOT NULL
                                    ); """

TaskSchema = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    task_name text NOT NULL,
                                    task_status text NOT NULL,
                                    task_priority text NOT NULL
                                );"""

ChatHistorySchema = """CREATE TABLE IF NOT EXISTS chat_history (
                                    id integer PRIMARY KEY,
                                    user_input text NOT NULL,
                                    bot_response text NOT NULL,
                                    timestamp text NOT NULL
                                );"""

if __name__ == '__main__':
    manageDatabase()
```