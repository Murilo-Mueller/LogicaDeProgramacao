codigo = 0
veiculos = 0
acidentes = 0
maior = 0
menor = float('inf')
cidadeMaior = 0
cidadeMenor = 0
somaVeiculoSC = 0
somaVeiculoRS = 0
somaVeiculoPR = 0
somaAcidenteSC = 0
somaAcidenteRS = 0
somaAcidentePR = 0
for contador in range (12):
    codigo = int(input("Digite o código da cidade "))
    veiculos = int(input("Digite o número de veículos de passeio "))
    acidentes = int(input("Digite o número de acidentes de trânsito com vítimas "))
    if acidentes > maior:
        maior = acidentes
        cidadeMaior = codigo
    if acidentes < menor:
        menor = acidentes
        cidadeMenor = codigo
    if codigo <= 14:
        somaVeiculoSC += veiculos
        somaAcidenteSC += acidentes
    elif codigo >= 31:
        somaVeiculoPR += veiculos
        somaAcidentePR += acidentes
    else:
        somaVeiculoRS += veiculos
        somaAcidenteRS += acidentes
print ("O maior índice de acidentes de trânsito é da cidade " , cidadeMaior , "com um índice de" , maior , ". O menor índice de acidentes de trânsito é da cidade " , cidadeMenor , "com um índice de " , menor , ". A média total de veículos é " , ((somaVeiculoSC + somaVeiculoRS + somaVeiculoPR) / 3) , ". A média de veículos em Santa Catarina é  " , (somaVeiculoSC / 4) , ". A média de veículos em Rio Grande do Sul é  " , (somaVeiculoRS / 4) , ". A média de veículos no Paraná é  " , (somaVeiculoPR / 4) , ". A média de acidentes com vítimas em Santa Catarina é" , (somaAcidenteSC / 4) , ". O total de acidentes em Santa Catarina é " , somaAcidenteSC , ". O total de acidentes em Rio Grande do Sul é " , somaAcidenteRS ,"e o total de acidentes no Paraná é " , somaAcidentePR)