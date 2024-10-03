class persona:
    def __init__(self, nom):
        self.nom = nom
    
    def saluda (self,nom2):
        print  (f"Hola {nom2}, soc el {self.nom} ")



demanar_nom =  input("Quin es el teu nom? ")
p1 =  persona ("Manel")
p1.saluda(demanar_nom)