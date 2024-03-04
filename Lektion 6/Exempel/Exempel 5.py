# Kontrollera om en fil existerar
import os
if os.path.exists('new_file.txt'):
    print("Filen existerar.")
else:
    print("Filen existerar inte.")
