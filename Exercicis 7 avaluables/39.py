# Algorisme que llegeixi nombres enters fins trobar 0, i ens mostri el màxim, el mínim i la mitjana de tots ells. Pensa com haurem d'inicialitzar les variables.


maxim = None
minim = None
suma = 0
comptador = 0

while True:
    num = int(input("Introdueix un nombre (0 per acabar): "))
    
    if num == 0:
        break  # Acaba el bucle si es troba el número 0
    
    if maxim is None or num > maxim:
        maxim = num
    
    if minim is None or num < minim:
        minim = num
    
    suma += num
    comptador += 1

# resultats

if comptador > 0:
    mitjana = suma / comptador
    print(f"Màxim: {maxim}, Mínim: {minim}, Mitjana: {mitjana:.2f}")
else:
    print("No s'ha introduït cap nombre vàlid.")
