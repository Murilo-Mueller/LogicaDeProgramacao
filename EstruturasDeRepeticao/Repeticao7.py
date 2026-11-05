numero = 1
contagem = 0
media = 0
soma = 0
while numero >= 0:
        numero = float(input("Escreva um número "))
        if numero >= 0:
            soma += numero
            contagem += 1
print ("A média dos números positivos é " , (soma / contagem))