numero = 0
contadorValido = 0
maiorTemperatura = 0
somaValido = 0
contadorTotal = 0
while numero != 999:
    numero = float(input("Escreva um número "))
    if numero == 999:
        break
    else:
        if (numero > -50) and (numero < 150):
            contadorTotal += 1
            if (numero >= 20 and numero <= 80) and (numero % 5 == 0) and (numero % 10 != 0):
                contadorValido += 1
                somaValido += numero
                if numero > maiorTemperatura:
                    maiorTemperatura = numero
print ("Foram " , contadorValido , " números válidos. A maior temperatura válida foi " , maiorTemperatura , " e o percentual válido sobre o total digitado foi de " , ((contadorValido * 100) / contadorTotal))