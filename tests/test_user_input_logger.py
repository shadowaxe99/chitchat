```python
import unittest
from src.user_input_logger import logUserInput

class TestUserInputLogger(unittest.TestCase):

    def setUp(self):
        self.user_input = "Hello, Chat2Code bot!"
        self.bot_response = "Hello, user! How can I assist you today?"

    def test_logUserInput(self):
        log = logUserInput(self.user_input, self.bot_response)
        self.assertIsNotNone(log)
        self.assertEqual(log['user_input'], self.user_input)
        self.assertEqual(log['bot_response'], self.bot_response)

if __name__ == '__main__':
    unittest.main()
```