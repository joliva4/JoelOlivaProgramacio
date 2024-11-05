# diem que introdueixi els ingressos per a cada mes

ingressos = []
for i in range(12):
    ing = float(input(f"Ingressos del mes {i+1}: "))
    ingressos.append(ing)

# es demana la quantitat a cercar
quantitat_a_cercar = float(input("Introdueix la quantitat a cercar: "))

# Es comprova si existeix dins del vector d'ingressos
if quantitat_a_cercar in ingressos:
    print("La quantitat existeix dins dels ingressos.")
else:
    print("La quantitat no existeix dins dels ingressos.")
