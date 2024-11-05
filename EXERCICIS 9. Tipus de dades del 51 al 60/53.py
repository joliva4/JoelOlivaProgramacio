notes_juntes = []
nota = int(input("Introdueix la nota: "))

while nota != "":
    notes_juntes.append(float(nota))
    nota = input("Nota del alumne (deixa-ho en blanc per acabar : )")

aprovats =  [nota for nota in notes_juntes if nota >= 5]

if (len(notes_juntes)) > 0:
    percentatje_aprovats = - (aprovats / len(notes_juntes)) *100
    print(f"El percentatge d'alumnes aprovats és: {percentatje_aprovats:.2f}%")
    
else:
    print("No hi ha notes")