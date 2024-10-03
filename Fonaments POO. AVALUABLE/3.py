class persona:
    def __init__(self, nom, edat):
        self.nom = "Manel"
        self.edat = "19"
    
    def presentacio (self):
        return  f"Hola soc el  {self.nom} i tinc {self.edat} anys"


p1 =  persona("Manel", "19")

print (p1)  # Output: Manel
print (p1.presentacio())  # Output: Hola soc el  Manel,