


class calculadora:
    @staticmethod
    def sumar (a,b):
        return a + b
    
    @staticmethod
    def resta (a,b):
        return a - b
    
    @staticmethod
    def multiplicar (a,b):
        return a * b
    
    @staticmethod
    def dividir (a,b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return  a / b
    

    # Demanar a l'usuari que introdueixi dos números
numero1 = float(input("Introdueix el primer  número: "))
numero2 = float(input("Introdueix el segon número: "))


    # Calcular i mostrar els resultats
suma = calculadora.sumar(numero1,numero2)
resta  = calculadora.resta(numero1,numero2)
multiplicar =  calculadora.multiplicar(numero1,numero2)
dividir =  calculadora.dividir(numero1,numero2)


print (f"el resultat es... {suma}")
print  (f"el resultat es... {resta}")
print (f"el resultat es... {multiplicar}")
print (f"el resultat es... {dividir}")











