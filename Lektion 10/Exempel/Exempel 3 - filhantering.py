    # Öppna en textfil för att lägga till i loggen
try:
    with open('python_log.txt', 'a') as output_file:    
        try:
            with open('new_file.txt', 'r') as file:
                content = file.read()
            output_file.write("Innehåll i filen:\n")
            output_file.write(content + "\n")
        except FileNotFoundError:
            output_file.write("Kunde inte hitta filen.\n")
        except IOError:
            output_file.write("Ett IO-fel inträffade när filen skulle läsas.\n")
        except Exception as e:
            output_file.write("Ett oväntat fel inträffade: " + str(e) + "\n")
except Exception as p:
            write("Ett oväntat fel inträffade: " + str(p) + "\n")
        
