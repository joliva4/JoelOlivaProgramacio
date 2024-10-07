nota = int (input("Introdueix el puntuatje "))
edat = int (input("Introdueix l'edat "))
sexe =  input("Introdueix el sexe ")

if nota >= 5 and edat >= 18 and sexe == "F":
    print("ACCEPTADA")

elif  nota >= 5 and edat >= 18 and sexe == "M":
    print("Possible ")

else:
    print("No ACCEPTADA ")



