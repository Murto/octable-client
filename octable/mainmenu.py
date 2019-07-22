from PyQt5.QtWidgets import QApplication, QBoxLayout, QLabel, QListWidget, QPushButton, QWidget
from PyQt5.QtCore import Qt

class MainMenu(QWidget):

  def __init__(self):
    super().__init__()
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    welcome = QLabel('Welcome to the Octable client')
    layout.addWidget(welcome, alignment=Qt.AlignCenter)
    createCharacterButton = QPushButton('Create Character')
    layout.addWidget(createCharacterButton, alignment=Qt.AlignCenter)
    manageCharactersButton = QPushButton('Manage Characters')
    layout.addWidget(manageCharactersButton, alignment=Qt.AlignCenter)
    settingsButton = QPushButton('Settings')
    layout.addWidget(settingsButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)
