with open('special_characters.txt', 'w', encoding='utf-8') as file:
    # Ny rad
    file.write("En rad med en ny rad.\n")
    
    # Tab
    file.write("En rad med en tab.\t")
    
    # Backslash
    file.write("En rad med ett backslash: \\")
    
    # Enkla citattecken
    file.write("En rad med enkla citattecken: \'")
    
    # Dubbla citattecken
    file.write("En rad med dubbla citattecken: \"")
    
    # Vagnretur
    file.write("\nEn rad med vagnretur.\r")
    
    # Formfeed
    file.write("\nEn rad med formfeed.\f")
    
    # Vertikal tab
    file.write("\nEn rad med vertikal tab.\v")
    
    # Hexadecimalt escape-tecken
    file.write("\nHexadecimalt escape-tecken: \x41")  # Detta kommer att skriva ut 'A'
    
    # Oktal escape-tecken
    file.write("\nOktal escape-tecken: \101")  # Detta kommer att skriva ut 'A'
    
    # Unicode-tecken (α)
    file.write("\nUnicode-tecken: α")
