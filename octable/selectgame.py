from PyQt5.QtWidgets import QBoxLayout, QListWidget, QPushButton, QWidget
from PyQt5.QtCore import Qt

class SelectGame(QWidget):

  def __init__(self):
    super().__init__()
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.backButton = QPushButton('Back')
    layout.addWidget(self.backButton, alignment=Qt.AlignCenter)
    self.installGamesButton = QPushButton('Install Games')
    layout.addWidget(self.installGamesButton, alignment=Qt.AlignCenter)
    self.gamesList = QListWidget()
    layout.addWidget(self.gamesList, alignment=Qt.AlignCenter)
    self.selectButton = QPushButton('Select')
    layout.addWidget(self.selectButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def setBackCallback(self, callback):
    self.backButton.clicked.connect(callback)

  def setInstallGamesCallback(self, callback):
    self.installGamesButton.clicked.connect(callback)

  def setSelectCallback(self, callback):
    self.selectButton.clicked.connect(callback)
