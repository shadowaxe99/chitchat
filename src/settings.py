```python
# src/settings.py

# Importing required libraries
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GPT-based Language Model
GPT_MODEL = os.getenv('GPT_MODEL')

# Chat2Code Bot API
CHAT2CODE_API = os.getenv('CHAT2CODE_API')

# Database
DATABASE = os.getenv('DATABASE')

# User Preferences Schema
UserPreferencesSchema = {
    "response_time": float,
    "task_categorization": str,
    "notification_preferences": str
}

# Task Schema
TaskSchema = {
    "task_id": int,
    "task_description": str,
    "task_priority": int,
    "task_status": str
}

# Chat History Schema
ChatHistorySchema = {
    "user_id": int,
    "chat_id": int,
    "message": str,
    "timestamp": str
}

# DOM Element IDs
DOM_Element_IDs = {
    "chatDisplay": "chatDisplay",
    "taskListView": "taskListView",
    "settingsView": "settingsView"
}

# Message Names
MessageNames = {
    "ChatMessage": "ChatMessage",
    "TaskMessage": "TaskMessage",
    "ReminderMessage": "ReminderMessage"
}
```