```python
import unittest
from src.data_security import secureData

class TestDataSecurity(unittest.TestCase):

    def setUp(self):
        self.data = "Sensitive User Data"

    def test_secureData(self):
        secured_data = secureData(self.data)
        self.assertNotEqual(secured_data, self.data, "Data should be secured and not equal to original")

    def test_secureData_not_empty(self):
        secured_data = secureData(self.data)
        self.assertTrue(secured_data, "Secured data should not be empty")

    def test_secureData_type(self):
        secured_data = secureData(self.data)
        self.assertIsInstance(secured_data, str, "Secured data should be a string")

if __name__ == '__main__':
    unittest.main()
```