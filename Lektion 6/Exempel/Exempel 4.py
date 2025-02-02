# Läsa radvis från en fil
with open('new_file.txt', 'r') as file:
    for row in file:
        print(row.strip())  # Tar bort eventuella mellanslag och radbrytningar
