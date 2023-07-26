```python
import os
from cryptography.fernet import Fernet
from src.database_manager import DATABASE

class DataSecurity:
    def __init__(self):
        self.key = os.getenv('SECURITY_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        """Encrypts the data using Fernet symmetric encryption"""
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt_data(self, cipher_text):
        """Decrypts the data using Fernet symmetric encryption"""
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def secure_data(self, data, action):
        """Secures the data based on the action specified - encrypt or decrypt"""
        if action == 'encrypt':
            return self.encrypt_data(data)
        elif action == 'decrypt':
            return self.decrypt_data(data)
        else:
            raise ValueError("Invalid action. Choose between 'encrypt' and 'decrypt'.")

def secure_user_data():
    """Secures user data in the database"""
    data_security = DataSecurity()
    for table in DATABASE.tables:
        for row in table.rows:
            for column in row.columns:
                if column.type == 'text':
                    encrypted_data = data_security.secure_data(column.data, 'encrypt')
                    column.data = encrypted_data

def retrieve_user_data():
    """Retrieves and decrypts user data from the database"""
    data_security = DataSecurity()
    for table in DATABASE.tables:
        for row in table.rows:
            for column in row.columns:
                if column.type == 'text':
                    decrypted_data = data_security.secure_data(column.data, 'decrypt')
                    column.data = decrypted_data
```