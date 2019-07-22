from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt

class MainMenu(QWidget):

  def __init__(self):
    super().__init__()
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.welcome = QLabel('Welcome to the Octable client')
    layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
    self.createCharacterButton = QPushButton('Create Character')
    layout.addWidget(self.createCharacterButton, alignment=Qt.AlignCenter)
    self.manageCharactersButton = QPushButton('Manage Characters')
    layout.addWidget(self.manageCharactersButton, alignment=Qt.AlignCenter)
    self.settingsButton = QPushButton('Settings')
    layout.addWidget(self.settingsButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def setCreateCharacterCallback(self, callback):
    self.createCharacterButton.clicked.connect(callback)

  def setManageCharactersCallback(self, callback):
    self.manageCharactersButton.clicked.connect(callback)

  def setSettingsCallback(self, callback):
    self.settingsButton.clicked.connect(callback)
