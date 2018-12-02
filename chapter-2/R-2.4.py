class Flower:
  """ Represents a flower in a flower shop"""

  def __init__(self, name, petals, price):
    self._name = name
    self._petals = petals
    self._price = price

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_petals(self):
    return self._petals

  def set_petals(self, petals):
    self._petals = petals

  def get_price(self):
    return self._price

  def set_price(self, price):
    self._price = price

if __name__ == '__main__':
  flower = Flower('lorem', 3, 15)

  print(flower.get_name())
  flower.set_name('ipsum')
  print(flower.get_name())
