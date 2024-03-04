import os

# Ange sökvägen till filen
fil_sökväg = 'new_file.txt'

# Kontrollera om filen finns innan du försöker radera den
if os.path.exists(fil_sökväg):
    # Radera filen
    os.remove(fil_sökväg)
    print(f'Filen {fil_sökväg} har raderats.')
else:
    print(f'Filen {fil_sökväg} finns inte.')
