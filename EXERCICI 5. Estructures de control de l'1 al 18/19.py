totsPositius = True 
for i in range (10):
    num = int(input("Posa un enter "))
    if  num < 0:
        totsPositius = False

if totsPositius == True:
    print ("Tots possitius")

else:
    print ("Hi ha algun negatiu")
print(totsPositius)