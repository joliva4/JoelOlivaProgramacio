while True:

    # Sol·licitem a l'usuari dos nombres
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))

    # Si els dos nombres són 0, finalitzem el bucle
    if num1 == 0 and num2 == 0:
        print("S'han introduït dos zeros, finalitzant el programa.")
        break

    # Si no són zeros, fem la suma i la imprimim
    suma = num1 + num2
    print(f"La suma de {num1} i {num2} és: {suma}")
