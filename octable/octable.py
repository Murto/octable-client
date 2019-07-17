import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt

class OctableWidget(QWidget):

  def __init__(self):
    super().__init__()
    self.setLayoutMainMenu()

  def setLayoutMainMenu(self):
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    self.welcome = QLabel('Welcome to the Octable client')
    layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
    self.setLayout(layout)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
