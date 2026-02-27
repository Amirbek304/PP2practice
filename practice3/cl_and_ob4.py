class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(myobject):
    print("Hello, my name is " + myobject.name)

p1 = Person("Baktygul", 56)
p1.greet()