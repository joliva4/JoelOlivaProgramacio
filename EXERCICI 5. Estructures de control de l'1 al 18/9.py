nombre1= float(input("Introduix el primer nombre "))
nombre2= float(input("Introduix el segon nombre "))
nombre3= float(input("Introduix el tercer nombre "))

if nombre1 >= nombre2 and nombre1 >= nombre3:
    if nombre2 >= nombre3:
        print(nombre1, nombre2, nombre3)
    else:
        print(nombre1, nombre3, nombre2)
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    if nombre1 >= nombre3:
        print(nombre2, nombre1, nombre3)
    else:
        print(nombre2, nombre3, nombre1)
else:
    if nombre1 >= nombre2:
        print(nombre3, nombre1, nombre2)
    else:
        print(nombre3, nombre2, nombre1)