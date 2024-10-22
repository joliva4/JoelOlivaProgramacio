# Tenint en compte que la clau és "eureka", escriure un algorisme que ens demani una clau. Únicament tenim 3 intents per encertar, si fallem els 3 intents ens mostrarà un missatge indicant-nos que hem esgotat els intents. Si encertem la clau, sortirem directament.


clau = "eureka"

for i  in range(3):
    contrasenya = input("Introdueix la clau: ")
    if contrasenya == clau:
        print("La clau és correcta")
        break
        
    elif contrasenya != clau:
        print("s'han acabat els intents ")
        
