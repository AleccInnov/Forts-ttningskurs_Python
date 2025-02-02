class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        print(f"{self.name} är en {self.color} blomma.")

class Rose(Flower):
    def __init__(self, fragrance, name, color):
        super().__init__(name, color)
        self.fragrance = fragrance

    def display_info(self):
        print(f"{self.name} är en {self.color} ros som doftar {self.fragrance}.")

rose = Rose("Ros", "röd", "sött")
rose.display_info()
