classificacao = 1
naoPerecivel = 0
perecivel = 0
vestuario = 0
higiene = 0
limpeza = 0
while classificacao != 0:
    classificacao = int(input("Escreva o código do produto "))
    if classificacao == 0:
        break
    else:
        if classificacao == 1:
            naoPerecivel += 1
        elif classificacao <= 4:
            perecivel += 1
        elif classificacao <= 6:
            vestuario += 1
        elif classificacao == 7:
            higiene += 1
        elif classificacao <= 15:
            limpeza += 1
        else:
            print("Erro")
print ("Alimento não-perecível: " , naoPerecivel , "\nAlimento perecível: " , perecivel , "\nVestuário: " , vestuario , "\nHigiene pessoal: " , higiene , "\nLimpeza e utensílios domésticos: " , limpeza)