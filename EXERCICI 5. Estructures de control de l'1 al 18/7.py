base = int(input("La base es "))
exponent =  int(input("El exponente es "))

if exponent >= 0:
    print(f"La potencia es  {base ** exponent} ")

elif exponent == 0:
    print(f"El resultat es 1 ")

elif exponent < 0:
    print (f"El resultat es {1/abs (exponent)}")

