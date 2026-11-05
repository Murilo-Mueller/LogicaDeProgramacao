idade = 0
nota = 0
contagem4 = 0
somaIdade4 = 0
soma1 = 0
contagem2 = 0
print ("Péssimo = 1\nRegular = 2\nBom = 3\nExcelente = 4")
for contador in range (7):
    nota = int(input("Digite que nota você dá "))
    idade = int(input("Escreva sua idade "))
    if nota == 4:
        contagem4 += 1
        somaIdade4 += idade
    elif nota == 1:
        soma1 += 1
    elif nota == 2:
        contagem2 += 1
print ("A média de idade dos clientes que avaliaram como excelente foi de " , (somaIdade4 / contagem4) , ". O total de clientes que avaliaram como péssimo foi de " , soma1 , " e a porcentagem de clientes que avaliaram como bom em relação ao total foi de " , ((contagem2 * 100) / 7))
