from PyQt5.QtWidgets import QApplication, QStackedWidget
from mainmenu import MainMenu
from selectgame import SelectGame
import sys

def test():
  print("Hello, world!")

class OctableWidget(QStackedWidget):

  def __init__(self):
    super().__init__()
    self.mainmenu = MainMenu()
    self.selectgame = SelectGame()
    self.addWidget(self.mainmenu)
    self.addWidget(self.selectgame)
    self.mainmenu.setCreateCharacterCallback(self.showSelectGame)
    self.selectgame.setBackCallback(self.showMainMenu)
  
  def showMainMenu(self):
    self.setCurrentWidget(self.mainmenu)

  def showSelectGame(self):
    self.setCurrentWidget(self.selectgame)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
