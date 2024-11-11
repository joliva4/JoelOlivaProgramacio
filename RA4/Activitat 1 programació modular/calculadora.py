num1 = int(input("Possa el primer numero :"))
num2 = int(input("Possa el segon numero :"))
operacio = (input("Possa un sombol com (+, -, * o /) :"))    


def calculador(num1, num2, operacio):
    if operacio == "+":
        return num1 + num2
    
    elif operacio == "-":
        return num1 - num2
    
    elif operacio == "*":
        return num1 * num2
    
    elif operacio == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "No pots dividir per zero"
    else:
        return "No has introduit un operador valid"

resultat = calculador(num1, num2, operacio)

print(f"El resultat es: {resultat}")