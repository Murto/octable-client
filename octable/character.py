from entity import Entity

class Character(Entity):

  def __init__(self, game, attributes):
    super().__init__(attributes)
    self._game = game

  def getGame(self):
    return self._game
