btc = 0.5 
eth = 2
ripple = 1000

preu_btc = 27000
preu_ethereum = 1800
preu_ripple = 0.5


#calculem el que ens ha costat cada criptomoneda 
valor_bitcoin = preu_btc //2
valor_ethereum = eth *1800
valor_ripple = ripple *0.5

#Sumem lo que ens ha costat cada criptomoneda
valortotal = (preu_btc //2 + eth *1800 + ripple *0.5)


#Calculem els percentatges de cada criptomoneda
btc_percentage = (valor_bitcoin / valortotal)*100
eth_percentage = (valor_ethereum / valortotal) *100
xrp_percentage = (valor_ripple / valortotal) *100



#RENDIMENT DE LA INVERSIÓ
cost_total_inicial = 15000

roi = ((valortotal - cost_total_inicial) / cost_total_inicial)*100




print( valor_bitcoin, "€")
print( valor_ethereum, "€")
print( valor_ripple, "€")
print(valortotal, "€")
print (f"El percentatge de bitcoin es... {btc_percentage:.2f} &" )
print (f"El percentatge de ethereum es... {eth_percentage:.2f} %")
print (f"El percentatge de ripple es... {xrp_percentage:.2f} %")
print(f"El rendiment de la inversió es... {roi:.2f} %")
