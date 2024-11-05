# Demanem 10 valors a l'usuari i els emmagatzemem en un vector
vector = []
for i in range(10):
    valor = int(input(f"Introdueix el valor {i+1}: "))
    vector.append(valor)


# Demanem el valor
valor_a_cercar = int(input("Introdueix el valor a cercar: "))



# Busquem el valor dins del vector i mostrem la posició
if valor_a_cercar in vector:
    posicio = vector.index(valor_a_cercar)
    print(f"El valor es troba a la posició {posicio}.")
else:
    print("El valor no es troba dins del vector.")
