#Imprimeix els nombres imparells fins el 100 i els compti i ens digui quants n'hi ha.

contador = 0
imparells = []

for i in range(101):
    if i % 2 != 0:
        contador += 1
        imparells.append(str(i))  # Afegim els números imparells com a string a la llista

# Imprimim els números imparells separats per un -
print(f"ELS NÚMEROS IMPARELLS SÓN: {'-'.join(imparells)}")
print(f"HI HA UN TOTAL DE {contador} NOMBRES IMPARELLS FINS A 100.")

