
class Producte:
    def __init__(self, nom, preu, descompte):
        self.nom = nom
        self.preu = preu
        self.descompte = descompte

    def preu_descompte(self):
# Calculem el preu amb descompte
        preu_final = self.preu - (self.preu*(self.descompte / 100))
        return preu_final
    


# Demanar a l'usuari que introdueixi el nom, preu i descompte
nom = input("Introdueix  el nom del producte: ")
preu = float(input("Introdueix  el preu del producte: "))
descompte = float(input("Introdueix  el descompte del producte: "))


# Crear una instància de Producte
Producte = Producte(nom, preu, descompte)

preu_final = Producte.preu_descompte()

print(f"El producte '{Producte.nom}' té un preu amb descompte de: {preu_final:.2f} €")

