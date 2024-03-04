with open('new_file_copy.txt', 'r') as file:
    file.seek(5)  # Flytta filpekaren till position 5
    content = file.read(10)  # Läs 10 tecken från position 5
    print(content)
