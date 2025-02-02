# Övning: Använd en debugger för att hitta och åtgärda felet i koden.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n + 1)

result = factorial(5)
print("Factorial of 5 is:", result)
