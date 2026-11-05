numero = int(input("Escreva um número"))
valor = 0
if (numero % 2 == 0):
    valor = numero
else:
    valor = numero - 1
print (valor)
vezes = int(valor / 2)
for contador in range (vezes):
    print (valor - 2)
    valor = valor - 2