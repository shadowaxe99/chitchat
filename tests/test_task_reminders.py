```python
import unittest
from src.task_reminders import sendTaskReminder

class TestTaskReminders(unittest.TestCase):

    def setUp(self):
        self.task = {
            'id': 1,
            'title': 'Test Task',
            'description': 'This is a test task',
            'due_date': '2022-12-31',
            'status': 'pending'
        }

    def test_sendTaskReminder(self):
        # Test that the reminder is sent for pending tasks
        result = sendTaskReminder(self.task)
        self.assertTrue(result)

    def test_noReminderForCompletedTasks(self):
        # Test that no reminder is sent for completed tasks
        self.task['status'] = 'completed'
        result = sendTaskReminder(self.task)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
```