somaTotal = 0
numero = 1
contador = 0
while numero != 0:
    numero = float(input("Escreva um número "))
    if (numero % 2 == 0):
        somaTotal += numero
        contador += 1
print ("A média dos números pares é " , ((somaTotal) / (contador - 1)))