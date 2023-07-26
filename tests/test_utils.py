```python
import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.utilFunction = utils.utilFunction

    def test_utilFunction(self):
        # Test the utilFunction with some inputs
        result = self.utilFunction("Test Input")
        self.assertEqual(result, "Expected Output")

if __name__ == '__main__':
    unittest.main()
```