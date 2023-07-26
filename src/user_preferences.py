```python
import sqlite3
from sqlite3 import Error
from src.database_manager import DATABASE

class UserPreferences:
    def __init__(self):
        self.conn = None
        self.create_table()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(DATABASE)
        except Error as e:
            print(e)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        self.create_connection()
        try:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS UserPreferences (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    response_time INTEGER,
                    task_categorization TEXT,
                    notification_preferences TEXT
                )
            """)
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def setUserPreferences(self, response_time, task_categorization, notification_preferences):
        self.create_connection()
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO UserPreferences(response_time, task_categorization, notification_preferences)
                VALUES(?,?,?)
            """, (response_time, task_categorization, notification_preferences))
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def getUserPreferences(self):
        self.create_connection()
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM UserPreferences ORDER BY id DESC LIMIT 1")
            return cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            self.close_connection()
```