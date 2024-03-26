try:
    file = open("fil_som_inte_finns.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Filen kunde inte hittas.")
