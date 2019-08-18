class Entity:

  def __init__(self, attributes):
    self.attributes = attributes

  def getAttribute(self, identifier):
    return self.attribute[identifier]

  def addAttribute(self, identifier, attribute):
    self.attributes[identifier] = attribute

  def removeAttribute(self, identifier):
    del self.attributes[identifier]
