nome = "a"
nota  = 0
somaNota = 0
contagem7 = 0
for contador in range (35):
    nome = input("Escreva o seu nome ")
    nota = float(input("Escreva a sua nota "))
    somaNota += nota
    if nota > 7:
        contagem7 += 1
print ("A média geral da turma foi de " , (somaNota / 35) , " e a quantidade de alunos que tiveram nota acima de 7 foi de " , contagem7)
