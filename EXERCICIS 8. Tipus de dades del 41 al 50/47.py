frase = input("Introdueix una frase : ")
caracter1 = input("Introdueix un caracter : ")
caracter2 = input("Introdueix un altre caracter : ")


caracter_sub = frase.replace(caracter1, caracter2)
print(f"La frase amb els caracters substitüits es : {caracter_sub}")