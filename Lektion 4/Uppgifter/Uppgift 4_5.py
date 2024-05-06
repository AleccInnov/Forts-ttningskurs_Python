class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        print(f"{self.name} är en {self.color} blomma.")

class Tulip(self):
    def __init__(self, name, color, petals):
        super().__init__(name, color)
        self.petals = petals

    def display_info(self):
        print(f"{self.name} är en {self.color} tulpan {self.petals} kronblad.")

tulip = Tulip("Vanlig tulpan", "röd", 6)
tulip.display_info()
