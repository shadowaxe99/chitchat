```python
import unittest
from src.task_adjustment import adjustTask

class TestTaskAdjustment(unittest.TestCase):

    def setUp(self):
        self.task_list = [
            {"id": 1, "task": "Task 1", "priority": "High", "status": "Incomplete"},
            {"id": 2, "task": "Task 2", "priority": "Medium", "status": "Incomplete"},
            {"id": 3, "task": "Task 3", "priority": "Low", "status": "Incomplete"}
        ]

    def test_adjustTask(self):
        # Test case: Adjusting task priority
        updated_task_list = adjustTask(self.task_list, 1, "priority", "Medium")
        self.assertEqual(updated_task_list[0]["priority"], "Medium")

        # Test case: Adjusting task status
        updated_task_list = adjustTask(self.task_list, 2, "status", "Complete")
        self.assertEqual(updated_task_list[1]["status"], "Complete")

        # Test case: Invalid task id
        with self.assertRaises(ValueError):
            adjustTask(self.task_list, 5, "status", "Complete")

        # Test case: Invalid field
        with self.assertRaises(ValueError):
            adjustTask(self.task_list, 1, "invalid_field", "Complete")

if __name__ == '__main__':
    unittest.main()
```