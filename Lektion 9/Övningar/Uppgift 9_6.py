#Uppgift: Ändra koden för att ge tydligare felmeddelanden
#som hjälper användaren att själv se vad felet är.

def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)
