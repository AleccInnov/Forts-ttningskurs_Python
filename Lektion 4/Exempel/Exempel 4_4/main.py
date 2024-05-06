from car import Car, Motorcycle

# Skapa en instans av Car och Motorcycle
my_car = Car("Toyota", "Corolla", 2020, 4)
my_motorcycle = Motorcycle("Honda", "CBR500R", 2021, 500)

# Använd metoderna och visa informationen för fordonen
my_car.start()
my_car.display_info()

my_motorcycle.start()
my_motorcycle.display_info()

my_car.stop()
my_motorcycle.stop()
