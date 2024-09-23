
Ciutata = (input("Origen "))
Ciutatb = (input("Destinacio "))
HH = int(input("Quina hora es? "))
MM = int(input("Quins minuts son? "))
SS = int(input("Quins segons son? "))
Tempsviatge = int(input("Temps del trajecte en segons ? "))

#Passo el temps a Hores
calT_H = Tempsviatge //3600
Residu= Tempsviatge %3600

calT_M = Residu //60
calT_S = Residu %60



print (f"Arribaras a {Ciutatb} a les ", HH + calT_H, MM + calT_M, calT_S)