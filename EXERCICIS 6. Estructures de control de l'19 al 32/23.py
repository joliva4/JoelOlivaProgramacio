# Algorisme que donades les hores setmanals i el preu hora treballades, si aquestes passen de 40 hores les hores extraordinàries es pagaran 1,5 vegades la hora ordinària.

while  True:

    hores_setmanals = float(input("Introdueix les hores setmanals : "))
    preu_hora = float(input("Introdueix el preu hora : "))
    print (f"la  quantitat a pagar és {hores_setmanals * preu_hora}")
        

    if hores_setmanals > 40:
        hores_extraordinaries = preu_hora *1.5
        print (f"El preu de les hores extraordinàries és : ,{hores_extraordinaries}, hauras de pagar  {hores_setmanals * preu_hora + hores_extraordinaries}")

