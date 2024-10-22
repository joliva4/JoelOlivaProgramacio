# Llegir tres nombres que denoten una data (dia, mes, any). Comprovar que és una data vàlida. Si no és vàlida dona un missatge d'error. Si és vàlida escriure la data canviant el número del mes pel seu nom.


dia =  int(input("Introdueix el dia: "))
mes = int(input("Introdueix el mes: "))
any = int(input("Introdueix l'any: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("La data no es vàlida")
else:
    if mes == 1:
        print(f"{dia} de gener de {any}")
    elif mes == 2:
        print(f"{dia} de febrer de {any}")
    elif mes == 3:
        print(f"{dia} de març de {any}")
    elif mes == 4:
        print(f"{dia} d'abril de {any}")
    elif mes == 5:
        print(f"{dia} de maig de {any}")
    elif mes == 6:
        print(f"{dia} de juny de {any}")
    elif mes == 7:
        print(f"{dia} de juliol de {any}")
    elif mes == 8:
        print(f"{dia} d'agost de {any}")
    elif mes == 9:
        print(f"{dia} de setembre de {any}")
    elif mes == 10:
        print(f"{dia} d'octubre de {any}")
    elif mes == 11:
        print(f"{dia} de novembre de {any}")
    elif mes == 12:
        print(f"{dia} de desembre de {any}")
        