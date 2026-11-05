idade = 0
opiniao = 0
contagemBom = 0
contagemRegular = 0
for contador in range (15):
    idade = int(input("Escreva sua idade "))
    opiniao = int(input("Escreva sua opiniao (ótimo = 3, bom = 2, regular = 1) "))
    if opiniao == 2:
        contagemBom += 1
    elif opiniao == 1:
        contagemRegular += 1
print ("A quantidade de pessoas que respondeu regular foi de " , contagemRegular , " e a percentagem de pessoas que respondeu bom entre todos os espectadores analisados foi de " , ((contagemBom * 100) / 15))