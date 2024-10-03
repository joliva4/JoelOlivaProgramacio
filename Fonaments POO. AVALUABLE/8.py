import random
class Dau:
    @staticmethod
    def resultat ():
        return random.randint(1,6)
    
print (f"Els resultats dels llançaments son {Dau.resultat()},{Dau.resultat()},{Dau.resultat()},{Dau.resultat()}")