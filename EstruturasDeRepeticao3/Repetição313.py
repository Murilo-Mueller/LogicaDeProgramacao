pA = 0
pB = 1
contagem = 0
contagem5 = 0
pA = int(input("Escreva a população A "))
pB = int(input("Escreva a população B "))
while pA < pB:
    pA = ((pA * 103) / 100)
    pB = ((pB * 101.5) / 100)
    contagem += 1
    contagem5 += 1
    if contagem5 == 5:
        contagem5 = 0
        pA = ((pA * 93) / 100)
        pB = ((pB * 93) / 100)
print ("Levaram " , contagem , " anos para a população A passar a população B")