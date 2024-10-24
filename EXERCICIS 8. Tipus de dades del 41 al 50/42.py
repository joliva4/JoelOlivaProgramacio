# Realitzar un programa que comprova si una cadena llegida per teclat comença per una subcadena introduïda per teclat.


cadena1 = input("Possa una frase : ")
cadena2 = input("Possa una altre frase : ")

if cadena2 in cadena1 or cadena1 in cadena2:
    print(f"{cadena2} comença per una subcadena ")

