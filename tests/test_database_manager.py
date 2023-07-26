```python
import unittest
from src.database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db_manager = DatabaseManager(DATABASE)

    def test_create_user_preferences(self):
        user_preferences = {
            'response_time': 'fast',
            'task_categorization': 'priority',
            'notification_preferences': 'email'
        }
        self.db_manager.create_user_preferences(user_preferences)
        result = self.db_manager.get_user_preferences()
        self.assertEqual(result, user_preferences)

    def test_update_user_preferences(self):
        user_preferences = {
            'response_time': 'slow',
            'task_categorization': 'date',
            'notification_preferences': 'sms'
        }
        self.db_manager.update_user_preferences(user_preferences)
        result = self.db_manager.get_user_preferences()
        self.assertEqual(result, user_preferences)

    def test_create_task(self):
        task = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'priority': 'high',
            'status': 'pending'
        }
        self.db_manager.create_task(task)
        result = self.db_manager.get_task(task['title'])
        self.assertEqual(result, task)

    def test_update_task(self):
        task = {
            'title': 'Test Task',
            'description': 'This is an updated test task',
            'priority': 'low',
            'status': 'completed'
        }
        self.db_manager.update_task(task)
        result = self.db_manager.get_task(task['title'])
        self.assertEqual(result, task)

    def test_delete_task(self):
        task_title = 'Test Task'
        self.db_manager.delete_task(task_title)
        result = self.db_manager.get_task(task_title)
        self.assertIsNone(result)

    def test_create_chat_history(self):
        chat_history = {
            'user_input': 'Hello, Chat2Code bot!',
            'bot_output': 'Hello, user!'
        }
        self.db_manager.create_chat_history(chat_history)
        result = self.db_manager.get_chat_history(chat_history['user_input'])
        self.assertEqual(result, chat_history)

    def test_delete_chat_history(self):
        user_input = 'Hello, Chat2Code bot!'
        self.db_manager.delete_chat_history(user_input)
        result = self.db_manager.get_chat_history(user_input)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
```