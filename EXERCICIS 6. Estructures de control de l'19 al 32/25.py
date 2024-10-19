suma_total = 0

# Demanem 10 números i els anem sumant
for i in range(10):
    num = float(input(f"Introdueix el número {i+1}: "))
    suma_total += num

# Calculem la mitjana
mitjana = suma_total / 10

# Mostrem el resultat
print(f"La mitjana aritmètica dels 10 números és: {mitjana}")
