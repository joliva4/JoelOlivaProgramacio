Nombre1= float(input("Introduix el primer nombre "))
Nombre2= float(input("Introduix el segon nombre "))
Nombre3= float(input("Introduix el tercer nombre "))

numeros = [Nombre1, Nombre2, Nombre3]

numeros_ordenats = sorted(numeros, reverse=True)

print ("Numeros de mes gran a mes petit: ", numeros_ordenats)
