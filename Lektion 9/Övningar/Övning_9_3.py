# Övning: Identifiera det logiska felet och korrigera koden för att
# få körbar kod.

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

numbers = []
print("Average:", calculate_average(numbers))
