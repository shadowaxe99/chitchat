```python
import openai
from settings import GPT_MODEL

class GPTModel:
    def __init__(self):
        self.model = GPT_MODEL
        self.api_key = "your_openai_api_key"  # Replace with your OpenAI API key
        openai.api_key = self.api_key

    def process_user_input(self, user_input):
        """
        Process user input using GPT-based language models
        """
        response = openai.Completion.create(
            engine=self.model,
            prompt=user_input,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def generate_task(self, bot_output):
        """
        Generate tasks based on bot outputs
        """
        task = self.process_user_input(bot_output)
        return task
```