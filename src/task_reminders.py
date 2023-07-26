```python
import time
from threading import Timer
from src.database_manager import DATABASE

class TaskReminder:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, task_id, reminder_time):
        """Add a new reminder for a task."""
        reminder = Timer(reminder_time, self.send_task_reminder, [task_id])
        self.reminders.append(reminder)
        reminder.start()

    def remove_reminder(self, task_id):
        """Remove a reminder for a task."""
        for reminder in self.reminders:
            if reminder.args[0] == task_id:
                reminder.cancel()
                self.reminders.remove(reminder)
                break

    def send_task_reminder(self, task_id):
        """Send a reminder for a task."""
        task = DATABASE.get_task(task_id)
        if task and not task['is_completed']:
            print(f"Reminder: You have a pending task: {task['name']}")

    def check_reminders(self):
        """Check if there are any reminders to be sent."""
        current_time = time.time()
        for reminder in self.reminders:
            if reminder.interval <= current_time:
                self.send_task_reminder(reminder.args[0])
                self.remove_reminder(reminder.args[0])

task_reminder = TaskReminder()
```