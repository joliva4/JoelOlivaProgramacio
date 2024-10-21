# Dissenya un algorisme corresponent a un programa que donada una frase acabada, compti el nombre de caràcters que hi apareixen a partir de la primera “a”.

frase = input("Possa una frase ")
comptador = 0

for lletra in frase:
    if lletra == "a":
        comptador += 1
        print(comptador)