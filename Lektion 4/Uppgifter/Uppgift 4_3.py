class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        self.sound = "Woof"

dog = Dog("Buddy")
dog.make_sound()
