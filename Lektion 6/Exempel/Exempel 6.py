# Öppnar en befintlig fil och lägger till mer data i slutet av den
with open('new_file.txt', 'a') as file:
    file.write('Mer data som läggs till i slutet av filen.')
