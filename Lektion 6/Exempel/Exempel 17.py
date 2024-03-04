with open('new_file_copy.txt', 'r') as file:
    lines = file.readlines()  # Läs in alla rader i en lista
    for line in lines:
        if 'Rad' in line:
            print(line)
