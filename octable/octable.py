import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QLabel, QListWidget, QPushButton, QWidget
from PyQt5.QtCore import Qt

class OctableWidget(QWidget):

  def __init__(self):
    super().__init__()
    self.setLayoutMainMenu()

  def setLayoutMainMenu(self):
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    welcome = QLabel('Welcome to the Octable client')
    layout.addWidget(welcome, alignment=Qt.AlignCenter)
    createCharacterButton = QPushButton('Create Character')
    layout.addWidget(createCharacterButton, alignment=Qt.AlignCenter)
    manageCharactersButton = QPushButton('Manage Characters')
    layout.addWidget(manageCharactersButton, alignment=Qt.AlignCenter)
    settingsButton = QPushButton('Settings')
    layout.addWidget(settingsButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)

  def setLayoutSelectGame(self):
    layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    backButton = QPushButton('back')
    layout.addWidget(backButton, alignment=Qt.AlignRight)
    installGamesButton = QPushButton('Install Games')
    layout.addWidget(installGamesButton, alignment=Qt.AlignCenter)
    gameList = QListWidget()
    layout.addWidget(gameList, alignment=Qt.AlignCenter)
    selectGameButton = QPushButton('Select Game')
    layout.addWidget(selectGameButton, alignment=Qt.AlignCenter)
    self.setLayout(layout)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = OctableWidget()
  main.show()
  sys.exit(app.exec_())
