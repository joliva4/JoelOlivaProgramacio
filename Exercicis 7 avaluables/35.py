# Dissenya un algorisme corresponent a un programa que donada una frase, determini si té més caràcters “b” que “c”.

frase = input("Introdueix una frase: ")

# Compta les 'b' i les 'c'
contador_c = frase.count("c") + frase.count("C")
contador_b = frase.count("b") + frase.count("B")

if contador_b > contador_c:
    print("La frase té més lletres 'b' que 'c'.")

elif contador_b < contador_c:
    print("La frase té més lletres 'c' que 'b'.")
    
else:
    print("La frase té les mateixes lletres 'c' que lletres 'b'.")
