from PyQt5.QtWidgets import QBoxLayout, QTableWidget, QPushButton, QWidget
from PyQt5.QtCore import Qt

class ManageCharacters(QWidget):

  def __init__(self):
    super().__init__()
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.backButton = QPushButton('Back')
    layout.addWidget(self.backButton, alignment=Qt.AlignCenter)
    self.characterList = QTableWidget()
    layout.addWidget(self.characterList, alignment=Qt.AlignCenter)
    self.viewButton = QPushButton('View')
    layout.addWidget(self.viewButton, alignment=Qt.AlignCenter)
    self.deleteButton = QPushButton('Delete')
    layout.addWidget(self.deleteButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def setBackCallback(self, callback):
    self.backButton.clicked.connect(callback)

  def setViewCallback(self, callback):
    self.viewButton.clicked.connect(callback)

  def setDeleteCallback(self, callback):
    self.deleteButton.clicked.connect(callback)
