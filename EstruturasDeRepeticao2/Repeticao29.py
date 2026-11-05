valor = 0
nome = "a"
for contador in range (3):
    nome = input("Escreva o seu nome ")
    valor = int(input("Escreva o valor das compras do ano passado "))
    if valor > 500000:
        print("Parabéns," , nome , ", você ganhou um bônus de 15% e o valor final a ser pago é " , ((valor * 85) / 100))
    else:
        print("Parabéns," , nome , ", você ganhou um bônus de 10% e o valor final a ser pago é " , ((valor * 90) / 100))
