import shutil

# Kopierar en fil till en annan plats
source_file = 'new_file.txt'
destination_file = 'new_file_copy.txt'

shutil.copy(source_file, destination_file)
print(f'{source_file} har kopierats till {destination_file}.')
