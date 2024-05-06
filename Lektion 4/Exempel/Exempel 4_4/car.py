class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} started.")
        else:
            print(f"{self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.make} {self.model} stopped.")
        else:
            print(f"{self.make} {self.model} is already stopped.")

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")
        if self.is_running:
            print("Status: Running")
        else:
            print("Status: Stopped")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def display_info(self):
        super().display_info()
        print(f"Engine Size: {self.engine_size}cc")


