while True:
    # Llegim les notes de l'alumne
    practica = float(input("Introdueix la nota de la part pràctica (1 a 10): "))
    problemes = float(input("Introdueix la nota de la part de problemes (1 a 10): "))
    teorica = float(input("Introdueix la nota de la part teòrica (1 a 10): "))

    # Comprovem si les tres notes són 0 per finalitzar
    if practica == 0 and problemes == 0 and teorica == 0:
        print("Totes les notes són 0, finalitzant el programa.")
        break

    # Comprovem si totes les notes estan entre 1 i 10

    if 1 <= practica <= 10 and 1 <= problemes <= 10 and 1 <= teorica <= 10:
        # Calculem la nota final segons els percentatges
        nota_final = (practica * 0.10) + (problemes * 0.50) + (teorica * 0.40)
        print(f"La nota final de l'alumne és: {nota_final:.2f}")


    else:
        # Si alguna nota no està en el rang, mostrem un error i demanem les notes de nou

        print("Error: totes les notes han d'estar entre 1 i 10. Torna a introduir les notes.")
