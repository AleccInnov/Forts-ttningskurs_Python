# Övning: Lägg till loggmeddelanden för att spåra variabler
# och körningsflöde och hitta vad som skapar det felaktiga svaret.

def calculate_area(length, width):
    area = length * width
    print("Length:", length)
    print("Width:", width)
    print("Area:", area)

calculate_area(10, "5")
