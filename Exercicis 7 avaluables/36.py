# Algorisme que determini quina és la primera vocal que trobem en una frase.

frase = input("Possa una frase: ")

primera_vocal = None

for lletra in frase:
    if lletra in "aeiouAEIOU":
        primera_vocal = lletra
        print(f"La primera vocal de la frase és {primera_vocal}")
        break
