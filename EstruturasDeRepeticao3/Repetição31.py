contagem = 0
numero = 0
for contador in range (80):
    numero = int(input("Escreva um número "))
    if numero >= 10 and numero <= 150:
        contagem += 1
print (contagem , "número(s) estava(m) no intervalo entre 10 e 150")
