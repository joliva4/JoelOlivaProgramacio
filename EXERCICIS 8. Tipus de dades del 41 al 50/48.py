frase = input("Introdueix una frase : ")
convertit = ""

for lletra in frase:
    if lletra.islower():
        convertit += lletra.upper()

    elif lletra.isupper():
        convertit += lletra.lower()
    
    else:
        convertit += lletra
    
print (f"La frase convertida es : {convertit}")