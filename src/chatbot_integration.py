```python
import requests
from settings import CHAT2CODE_API

class Chat2CodeIntegration:
    def __init__(self):
        self.api_url = CHAT2CODE_API

    def send_message(self, message):
        payload = {'message': message}
        response = requests.post(self.api_url, data=payload)
        return response.json()

    def receive_message(self):
        response = requests.get(self.api_url)
        return response.json()

def integrateChat2Code():
    chat2code = Chat2CodeIntegration()
    return chat2code
```