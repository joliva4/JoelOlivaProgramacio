Article1 = int(input("Preu del primer article "))
Article2 = int(input("Preu del segon article "))
Article3 = int(input("Preu del tercer article "))


Preuarticles = Article1 + Article2 + Article3

Percentatge = Preuarticles * 15/100

Preufinal = Preuarticles - Percentatge
print ("El preu final es", Preufinal)