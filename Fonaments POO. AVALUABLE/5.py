
import math


class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area (self):
        return math.pi * (self.radi **2)
    

# Demanar a l'usuari que introdueixi el radi
radi_text = float(input("Introdueix el radi del cercle: "))
cercle = Cercle(radi_text)

# Calcular i mostrar l'àrea
area = cercle.area()

print(f"L'àrea del cercle amb radi {radi_text} és: {area:.2f}")
