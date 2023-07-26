```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget

class UserInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Chatbot Assistant')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chatDisplay = QTextEdit()
        self.taskListView = QListWidget()
        self.settingsButton = QPushButton('Settings')

        self.layout.addWidget(self.chatDisplay)
        self.layout.addWidget(self.taskListView)
        self.layout.addWidget(self.settingsButton)

        self.settingsButton.clicked.connect(self.openSettings)

    def openSettings(self):
        # Open settings view
        pass

    def updateChatDisplay(self, message):
        self.chatDisplay.append(message)

    def updateTaskList(self, tasks):
        self.taskListView.clear()
        for task in tasks:
            self.taskListView.addItem(task)

    def loadSettings(self):
        # Load user preferences
        pass

def main():
    app = QApplication(sys.argv)

    ui = UserInterface()
    ui.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```