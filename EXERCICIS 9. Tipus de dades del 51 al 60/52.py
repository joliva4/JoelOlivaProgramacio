# Crea un programa que vagi demanant a l'usuari introduir números per teclat fins a introduir el número 0. Cada número introduït s'afegirà a una llista. Un cop introduïts tots els números, es mostrarà per pantalla  tots ells en una única línia, així com la suma de tots ells en una altra línia i la quantitat de números introduïts en una altra. S'haurà de validar que l'usuari no introdueixi caràcters no numèrics.

llista =  []
contador = 0
while True:
    numeros = int(input("Introdueix un numero : "))
    llista.append(numeros)
    contador = sum(llista)


    print (*llista, sep="-")
    print (contador)
    print (f"La suma de els numeros introduits és: {contador}")
    print (f"Hi han {len(llista)} numeros a la llista ")

    if  numeros == 0:
        break

