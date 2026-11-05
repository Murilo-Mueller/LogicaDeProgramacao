import random
numero = random.randint (1, 50)
errou = 1
for contador in range (5):
    num = int(input("Digite um valor "))
    if num == numero:
        print ("Acertou")
        errou = 0
        break
    elif num < numero:
        print ("Tente novamente, seu numero é maior")
    elif num > numero:
        print ("Tente novamente, seu numero é menor")
if errou == 1:
    print ("O número sorteado foi " , numero)