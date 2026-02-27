class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("My name is", self.name, "im", self.age)


s1 = Person("Amir", 17)
s1.introduce()