with open('new_file_copy.txt', 'r') as file:
    content = file.read(10)  # Läs de första 10 tecknen från filen
    print(content)
