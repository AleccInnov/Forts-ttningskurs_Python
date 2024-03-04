name = "Alice"
age = 30

# String-formatering med format() metoden
formatted_string1 = "Hej, mitt namn är {} och jag är {} år gammal.".format(name, age)

# F-formaterade strängar (f-strings)
formatted_string2 = f"Hej, mitt namn är {name} och jag är {age} år gammal."

# Procentformatering med % -operatorn
formatted_string3 = "Hej, mitt namn är %s och jag är %d år gammal." % (name, age)

# Metoden str.format() (Python 2 och senare)
formatted_string4 = "Hej, mitt namn är {name} och jag är {age} år gammal.".format(name=name, age=age)

# Format specifiers
num = 3.14159
formatted_string5 = "Pi med tre decimaler: {:.3f}".format(num)

# Multiple string concatenation
formatted_string6 = "Hej, mitt namn är " + name + " och jag är " + str(age) + " år gammal."

# Skriv ut de formaterade strängarna
print(formatted_string1)
print(formatted_string2)
print(formatted_string3)
print(formatted_string4)
print(formatted_string5)
print(formatted_string6)
