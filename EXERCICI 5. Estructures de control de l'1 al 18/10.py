
# no esta acabat, falta reviso


import math

x1 = float(input("Introdueix  el valor de x1: "))
x2 = float(input("Introdueix  el valor de x2: "))
y1 = float(input("Introdueix  el valor de y1: "))
y2 = float(input("Introdueix  el valor de y2: "))
r1 =  float(input("Introdueix  el valor de r1: "))
r2 =  float(input("Introdueix  el valor de r2: "))





def classificacio(x1,y1,r1,x2,y2,r2):
    distancia = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)

# Possem les condicions...
    if distancia == 0 and r1 == r2:
        print ("concèntriques")
    elif distancia > r1 + r2:
        print ("exteriors")
    elif distancia == r1 + r2:
        print ("tangents exteriors")
    elif distancia < r1 + r2 and distancia > abs(r1 - r2):
        print ("assecants")
    elif distancia == abs(r1 - r2):
        print ("tangents interiors")
    elif distancia < abs(r1 - r2):
        print ("interiors")
    

