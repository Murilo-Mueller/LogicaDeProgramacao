numero = int(input("Escreva um número "))
intervalo = int(input("Escreva um intervalo "))
print (numero)
vezes = int(numero / intervalo)
for contador in range (vezes):
    print (numero - intervalo)
    numero = numero - intervalo
