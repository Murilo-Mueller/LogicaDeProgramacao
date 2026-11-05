contagem = 1
numero = 1
while numero != 0:
    numero = int(input("Digite um valor "))
    if numero < 0 and numero != 0:
        contagem += 1
print ("Foram " , contagem - 1 , " números negativos")