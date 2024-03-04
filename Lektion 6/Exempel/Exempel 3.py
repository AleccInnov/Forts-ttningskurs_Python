# Skriva flera rader till en fil
rader = ["Rad 1\n", "Rad 2\n", "Rad 3\n"]
with open('new_file.txt', 'w') as file:
    file.writelines(rader)
