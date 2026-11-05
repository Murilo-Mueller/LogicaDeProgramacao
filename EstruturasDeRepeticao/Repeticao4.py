salario = 0
filhos = 0
contagem = 0
somaSalario = 0
somaFilhos = 0
maiorSalario = 0
salario100 = 0
while salario >= 0:
    salario = float(input("Digite o seu salário "))
    if salario < 0:
        break
    filhos = int(input("Digite o número de filhos "))
    contagem += 1
    somaSalario += salario
    somaFilhos += filhos
    if salario > maiorSalario:
        maiorSalario = salario
    if salario < 100:
        salario100 += 1
print ("A média do salário da população é " , (somaSalario / contagem)  , ". A média do número de filhos é " , (somaFilhos / contagem) , ". O maior salário é " , maiorSalario , " e o percentual de pessoas com salário até R$100,00 é " , ((salario100 * 100) / contagem))