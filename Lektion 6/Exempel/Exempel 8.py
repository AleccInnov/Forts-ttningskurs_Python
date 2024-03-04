# Öppna filen för läsning
file = open('new_file.txt', 'r')

# Läs innehållet från filen
data = file.read()
print(data)

# Stäng filen manuellt
file.close()
