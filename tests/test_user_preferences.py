```python
import unittest
from src.user_preferences import UserPreferences

class TestUserPreferences(unittest.TestCase):

    def setUp(self):
        self.user_preferences = UserPreferences()

    def test_set_user_preferences(self):
        self.user_preferences.set_user_preferences(response_time=5, task_categorization=True, notification_preferences='email')
        self.assertEqual(self.user_preferences.response_time, 5)
        self.assertEqual(self.user_preferences.task_categorization, True)
        self.assertEqual(self.user_preferences.notification_preferences, 'email')

    def test_get_user_preferences(self):
        self.user_preferences.set_user_preferences(response_time=5, task_categorization=True, notification_preferences='email')
        preferences = self.user_preferences.get_user_preferences()
        self.assertEqual(preferences['response_time'], 5)
        self.assertEqual(preferences['task_categorization'], True)
        self.assertEqual(preferences['notification_preferences'], 'email')

if __name__ == '__main__':
    unittest.main()
```