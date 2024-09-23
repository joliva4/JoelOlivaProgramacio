monedade2 = int(input("Quantes monedes de 2€ tens? "))
monedade1 = int(input("Quantes monedes de 1€ tens ? "))
monedade20 = int(input("Quantes monedes de 20 centims tens? "))
monedade50 = int(input("Quantes monedes de 50 centims tens? "))
monedade10 = int(input("Quantes monedes de 10 centims tens? "))


total_centims = (monedade2 * 200) + (monedade1 * 100) + (monedade50 * 50) + (monedade20 * 20) + (monedade10 * 10)


# Euros sencers
euros = total_centims // 100

# Restant centims
centims = total_centims % 100

print (f"Total: {euros} euros i {centims} centims.")
