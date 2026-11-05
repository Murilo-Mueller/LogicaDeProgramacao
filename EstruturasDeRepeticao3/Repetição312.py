numero = 0
contagem3 = 0
soma2 = 0
for contador in range (10):
    numero = int(input("Escreva um número "))
    if numero % 3 == 0:
        contagem3 += 1
    if numero % 2 == 0:
        soma2 += numero
print (contagem3 , " números são múltiplos de 3 e a soma de todos os números pares é " , soma2)