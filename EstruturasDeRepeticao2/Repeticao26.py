numero = 1
somaPositivo = 0
somaNegativo = 0
listaPares = []
listaImpares = []
while numero != 0:
    numero = 0
    numero = int(input("Escreva um número "))
    if numero > 0:
        somaPositivo += numero
    else:
        somaNegativo += numero
    if numero % 2 == 0:
        listaPares.append (numero)
    else:
        listaImpares.append (numero)
print ("A soma dos números positivos é " , somaPositivo , ". A soma dos números negativos é " , somaNegativo , "\nNúmeros pares:" , "\n" , listaPares ,  "\nNúmeros impares:" , "\n" , listaImpares)
