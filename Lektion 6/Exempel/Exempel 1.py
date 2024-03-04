# Skriva till en fil
data = "Detta är innehållet som ska skrivas till filen."
with open('new_file.txt', 'w') as file:
    file.write(data)
