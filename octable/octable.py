from PyQt5.QtWidgets import QApplication, QStackedWidget
from mainmenu import MainMenu
import sys

def test():
  print("Hello, world!")

class OctableWidget(QStackedWidget):

  def __init__(self):
    super().__init__()
    self.addWidget(MainMenu())

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
