class persona:
    def __init__(self, nom, edat):
        self.nom = "Manel"
        self.edat = "19"
    
    def __str__(self):
        return  f"Nom: {self.nom}, Edat: {self.edat}"


p1 =  persona("Manel", "19")

print (p1)  # Output: Manel