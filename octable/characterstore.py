from attributes import NumberAttribute, StringAttribute
from character import Character

import logging
import json

# Syncs with an external file and updates changes to and from it
class CharacterStore:

  # Sync with the file 
  def __init__(self, path):
    self._logger = logging.getLogger(__name__)
    self._path = path
    self._characters = list()
    self.readOrCreate()

  def readOrCreate(self):
    try:
      with open(self._path, 'r') as f:
        content = f.read()
        try:
          serialized = json.loads(content)
          self._characters = self.deserialize(serialized)
        except json.JSONDecodeError as e:
          self._logger.error(f'JSON decoding error: {e.msg}')
          raise
    except FileNotFoundError:
      self._logger.info('File does not exist')
      self.create()

  def deserialize(self, serialized):
    GAME_FIELD = 'game'
    ATTRIBUTES_FIELD = 'attributes'
    ATTRIBUTE_TYPE_FIELD = 'type'
    # Format:
    # Array of Characters
    #   Each character has a `game` field
    #   Each character has an `attributes` object field
    #     The `attributes` object has attribute id fields
    #       Each id field has a value which is either a number or a string
    characters = list()
    for character in serialized:
      game = character[GAME_FIELD]
      attributes = dict()
      for identifier, value in character[ATTRIBUTE_FIELD].iteritems():
        attributeType = attribute[ATTRIBUTE_TYPE_FIELD]
        if (attributeType == NumberAttribute.TYPE):
          attributes[identifier] = NumberAttribute(value)
        elif (attributeType == StringAttribute.TYPE):
          attributes[identifier] = StringAttribute(value)
      characters.append(Character(game, attributes))
    return characters

  def create(self):
    self._logger.info('Creating new file')
    with open(self._path, 'w+') as f:
      f.write('[]')

  def write(self):
    with open(self._path, 'w+') as f:
      json.dump(self._characters, f)
