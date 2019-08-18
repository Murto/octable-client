class NumberAttribute:

  def __init__(self, number):
    assert(isinstance(number, int) or isinstance(number, float))
    self._value = number

  def getValue(self):
    return self._value

  def setValue(self, number):
    assert(isinstance(number, int) or isinstance(number, float))
    self._value = number
