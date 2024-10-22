# Algorisme que compti el nombre de "LA" dins una seqüència de caràcters.

frase = input("Escriu una frase : ")

comptador = 0
longitud = len(frase)

for i in range(longitud - 1):
    if frase[i:i + 2] == "LA":
        comptador += 1

print(f"Número d'aparicions de 'LA' es: {comptador}")
