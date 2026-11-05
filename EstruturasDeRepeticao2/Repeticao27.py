canal = 1
pessoas = 0
canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
soma = 0
while canal !=0:
    canal = int(input("Escreva o número do canal "))
    if canal == 0:
        break
    else:
        pessoas = int(input("Escreva quantas pessoas estavam assistindo "))
        if canal == 4:
            canal4 += pessoas
        elif canal == 5:
            canal5 += pessoas
        elif canal == 7:
            canal7 += pessoas
        elif canal == 12:
            canal12 += pessoas
soma = canal4 + canal5 + canal7 + canal12
print ("A porcentagem no canal 4 é " , ((canal4 * 100) / soma) , ", a porcentagem no canal 5 é " , ((canal5 * 100) / soma) , ", a porcentagem no canal 7 é " , ((canal7 * 100) / soma) , " e a porcentagem no canal 12 é " , ((canal12 * 100) / soma))
