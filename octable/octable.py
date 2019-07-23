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
    self.mainMenu = MainMenu()
    self.selectGame = SelectGame()
    self.settings = Settings()
    self.installGames = InstallGames()
    self.manageCharacters = ManageCharacters()
    self.viewCharacter = ViewCharacter()
    self.addWidget(self.mainMenu)
    self.addWidget(self.selectGame)
    self.addWidget(self.settings)
    self.addWidget(self.installGames)
    self.addWidget(self.manageCharacters)
    self.addWidget(self.viewCharacter)
    self.mainMenu.setCreateCharacterCallback(self.showSelectGame)
    self.mainMenu.setManageCharactersCallback(self.showManageCharacters)
    self.mainMenu.setSettingsCallback(self.showSettings)
    self.selectGame.setBackCallback(self.showMainMenu)
    self.selectGame.setInstallGamesCallback(self.showInstallGames)
    self.settings.setBackCallback(self.showMainMenu)
    self.installGames.setBackCallback(self.showSelectGame)
    self.manageCharacters.setBackCallback(self.showMainMenu)
    self.manageCharacters.setViewCallback(self.showViewCharacter)
    self.viewCharacter.setBackCallback(self.showManageCharacters)
  
  def showMainMenu(self):
    self.setCurrentWidget(self.mainMenu)

  def showSelectGame(self):
    self.setCurrentWidget(self.selectGame)

  def showManageCharacters(self):
    self.setCurrentWidget(self.manageCharacters)

  def showSettings(self):
    self.setCurrentWidget(self.settings)

  def showInstallGames(self):
    self.setCurrentWidget(self.installGames)

  def showViewCharacter(self):
    self.setCurrentWidget(self.viewCharacter)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
