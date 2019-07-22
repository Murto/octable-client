from PyQt5.QtWidgets import QBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import Qt

class Settings(QWidget):

  def __init__(self):
    super().__init__()
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.backButton = QPushButton('Back')
    layout.addWidget(self.backButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def setBackCallback(self, callback):
    self.backButton.clicked.connect(callback)
