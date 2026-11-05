jogador1 = 0
jogador2 = 0
ponto = 0
while True:
    ponto = int(input("Escreva o número do jogador que pontuou "))
    if ponto == 1:
        jogador1 += 1
    else:
        jogador2 += 1
    if jogador1 - jogador2 >= 2 and jogador1 >= 21:
        print ("Jogador 1 ganhou")
        break
    if jogador2 - jogador1 >= 2 and jogador2 >= 21:
        print ("Jogador 2 ganhou")
        break