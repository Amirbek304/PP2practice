class Animal:
    def speak(self):
        print("somr sounnd")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")
d = Dog()
d.speak()