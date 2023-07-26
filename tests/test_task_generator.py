```python
import unittest
from src.task_generator import generateTask

class TestTaskGenerator(unittest.TestCase):

    def setUp(self):
        self.user_input = "Create a new project named AI Chatbot Assistant"
        self.bot_output = "Sure, I have created a new project named AI Chatbot Assistant. What's next?"

    def test_generateTask(self):
        task = generateTask(self.user_input, self.bot_output)
        self.assertEqual(task['name'], 'Create a new project named AI Chatbot Assistant')
        self.assertEqual(task['status'], 'pending')

    def test_task_priority(self):
        task = generateTask(self.user_input, self.bot_output)
        self.assertEqual(task['priority'], 'normal')

    def test_task_completion(self):
        task = generateTask(self.user_input, self.bot_output)
        self.assertEqual(task['completion'], False)

if __name__ == '__main__':
    unittest.main()
```