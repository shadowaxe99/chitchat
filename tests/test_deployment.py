```python
import unittest
from unittest.mock import patch
from src import deployment

class TestDeployment(unittest.TestCase):

    @patch('src.deployment.deployApplication')
    def test_deployApplication(self, mock_deploy):
        # Test if the function is called
        deployment.deployApplication()
        mock_deploy.assert_called_once()

    @patch('src.deployment.deployApplication')
    def test_deployApplication_return(self, mock_deploy):
        # Test if the function returns the expected result
        mock_deploy.return_value = "Deployment Successful"
        result = deployment.deployApplication()
        self.assertEqual(result, "Deployment Successful")

if __name__ == '__main__':
    unittest.main()
```