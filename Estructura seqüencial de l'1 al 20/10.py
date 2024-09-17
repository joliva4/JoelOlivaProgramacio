Qualificacio1 = int (input("Nota primera activitat "))
Qualificacio2 = int(input("Nota segona activitat "))
Qualificacio3 = int(input("Nota tercera activitat "))
Examen = int(input("Nota Examen "))
Treball = int(input("Nota del treball "))



Notaactivitats = (Qualificacio1 + Qualificacio2 + Qualificacio3)/3 *55/100
Notaexamen = Examen *30/100
Notatreball = Treball *15/100
print ("La nota final es... ", Notaactivitats + Notaexamen + Notatreball )