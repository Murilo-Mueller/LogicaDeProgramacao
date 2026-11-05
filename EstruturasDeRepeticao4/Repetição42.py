temperatura = int(input("Escreva a temperatura "))
ciclo = 0
while temperatura <= 1000:
    ciclo += 1
    if temperatura < 800:
        temperatura += 50
    elif temperatura >= 800 and temperatura < 1000:
        temperatura += 20
print ("Foram necessários " , ciclo , " e a temperatura final é " , temperatura)

