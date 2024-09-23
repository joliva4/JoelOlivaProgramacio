Respostes_correctes = int(input("Numero de respostes correctes ")) 
Respostes_incorrectes = int(input("Numero de respostes incorrectes ")) 
Respostes_sensecontestar = int(input("Numero de respostes sense contestar ")) 


Correcta = Respostes_correctes *5
Incorrecta = Respostes_incorrectes * -1
Senseresposta = Respostes_sensecontestar

Correcta_calculada = Correcta
incorrecta_calculada = Incorrecta
Senseresposta_calculada = Senseresposta 

Resultat_final = (Correcta_calculada - incorrecta_calculada + Senseresposta_calculada) /10

#passar sobre 10 y no sobre 5

sobre10 = Resultat_final *2


print (sobre10)