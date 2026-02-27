class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Rinat")
p2 = Person("Serik")

p1.printname()
p2.printname()