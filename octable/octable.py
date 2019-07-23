from PyQt5.QtWidgets import QApplication, QStackedWidget
from mainmenu import MainMenu
from selectgame import SelectGame
from settings import Settings
from installgames import InstallGames
from managecharacters import ManageCharacters
from viewcharacter import ViewCharacter
import sys

def test():
  print("Hello, world!")

class OctableWidget(QStackedWidget):

  def __init__(self):
    super().__init__()
    self.mainmenu = MainMenu()
    self.selectgame = SelectGame()
    self.settings = Settings()
    self.installgames = InstallGames()
    self.managecharacters = ManageCharacters()
    self.viewcharacter = ViewCharacter()
    self.addWidget(self.mainmenu)
    self.addWidget(self.selectgame)
    self.addWidget(self.settings)
    self.addWidget(self.installgames)
    self.addWidget(self.managecharacters)
    self.addWidget(self.viewcharacter)
    self.mainmenu.setCreateCharacterCallback(self.showSelectGame)
    self.mainmenu.setManageCharactersCallback(self.showManageCharacters)
    self.mainmenu.setSettingsCallback(self.showSettings)
    self.selectgame.setBackCallback(self.showMainMenu)
    self.selectgame.setInstallGamesCallback(self.showInstallGames)
    self.settings.setBackCallback(self.showMainMenu)
    self.installgames.setBackCallback(self.showSelectGame)
    self.managecharacters.setBackCallback(self.showMainMenu)
    self.managecharacters.setViewCallback(self.showViewCharacter)
    self.viewcharacter.setBackCallback(self.showManageCharacters)
  
  def showMainMenu(self):
    self.setCurrentWidget(self.mainmenu)

  def showSelectGame(self):
    self.setCurrentWidget(self.selectgame)

  def showManageCharacters(self):
    self.setCurrentWidget(self.managecharacters)

  def showSettings(self):
    self.setCurrentWidget(self.settings)

  def showInstallGames(self):
    self.setCurrentWidget(self.installgames)

  def showViewCharacter(self):
    self.setCurrentWidget(self.viewcharacter)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
