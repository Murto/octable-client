import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QLabel, QListWidget, QPushButton, QStackedWidget, QWidget
from PyQt5.QtCore import Qt
from mainmenu import MainMenu

class OctableWidget(QStackedWidget):

  def __init__(self):
    super().__init__()
    self.addWidget(MainMenu())

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
