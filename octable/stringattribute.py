class StringAttribute:

  TYPE = 'STRING'

  def __init__(self, string):
    assert(isinstance(string, str))
    self._value = string

  def getValue(self):
    return self._value

  def setValue(self, string):
    assert(isinstance(string, str))
    self._value = string
