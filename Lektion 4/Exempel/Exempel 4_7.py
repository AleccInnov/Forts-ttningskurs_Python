class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

# Skapa en instans av Car
my_car = Car("Toyota", "Corolla", 2020)

# Använd display_info-metoden för att visa informationen om bilen
my_car.display_info()
