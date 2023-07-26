```python
import unittest
from src.gpt_model import GPT_MODEL, processUserInput

class TestGPTModel(unittest.TestCase):

    def setUp(self):
        self.gpt_model = GPT_MODEL
        self.user_input = "Hello, Chat2Code bot!"

    def test_gpt_model_instance(self):
        self.assertIsNotNone(self.gpt_model, "GPT model instance not created.")

    def test_process_user_input(self):
        response = processUserInput(self.user_input)
        self.assertIsNotNone(response, "No response from GPT model.")
        self.assertIsInstance(response, str, "Response from GPT model is not a string.")

if __name__ == '__main__':
    unittest.main()
```