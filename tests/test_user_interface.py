```python
import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.createUserInterface')
    def test_createUserInterface(self, mock_createUserInterface):
        user_interface.createUserInterface()
        mock_createUserInterface.assert_called_once()

    @patch('src.user_interface.QtWidgets.QApplication')
    @patch('src.user_interface.QtWidgets.QMainWindow')
    def test_realTimeChatDisplay(self, mock_QMainWindow, mock_QApplication):
        user_interface.realTimeChatDisplay()
        mock_QMainWindow.assert_called_once()
        mock_QApplication.assert_called_once()

    @patch('src.user_interface.QtWidgets.QApplication')
    @patch('src.user_interface.QtWidgets.QMainWindow')
    def test_taskListView(self, mock_QMainWindow, mock_QApplication):
        user_interface.taskListView()
        mock_QMainWindow.assert_called_once()
        mock_QApplication.assert_called_once()

    @patch('src.user_interface.QtWidgets.QApplication')
    @patch('src.user_interface.QtWidgets.QMainWindow')
    def test_customizationSettings(self, mock_QMainWindow, mock_QApplication):
        user_interface.customizationSettings()
        mock_QMainWindow.assert_called_once()
        mock_QApplication.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```