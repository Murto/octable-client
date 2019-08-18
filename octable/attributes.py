class NumberAttribute:

  TYPE = 'NUMBER'

  def __init__(self, number):
    assert(isinstance(number, int) or isinstance(number, float))
    self._value = number

  def getValue(self):
    return self._value

  def setValue(self, number):
    assert(isinstance(number, int) or isinstance(number, float))
    self._value = number

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
