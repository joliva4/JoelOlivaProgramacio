cadena = input("possa una frase : ")
caracter = input("Possa un caracter  : ")
cont = 0

for i in cadena:
    if i == caracter:
        cont += 1
        
print("El caracter apareix " + str(cont) + " vegades")

