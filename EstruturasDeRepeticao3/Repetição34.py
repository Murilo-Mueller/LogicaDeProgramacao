codigo = 0
valor = 0
prestacao = 0
bloqueador = 0
valorVista = 0
valorPrazo = 0
primeiraPrestacao = 0
for contador in range (15):
    codigo = int(input("Digite o código (1 para transação à vista e 2 para transação a prazo) "))
    valor = float(input("Escreva o valor da compra "))
    if codigo == 1:
        valorVista += valor
    elif codigo == 2:
        prestacao = int(input("Escreva em quantas vezes será pago "))
        valorPrazo += valor
    if prestacao == 3 and bloqueador == 0:
        primeiraPrestacao = valor
        bloqueador = 1
print ("O valor total das compras à vista foi " , valorVista , ". O valor total das compras a prazo foi " , valorPrazo , ". O valor total para as compras efetuadas foi " , (valorVista + valorPrazo) , " e o valor da primeira prestação das compras a prazo, sabendo que a mesma será paga em três vezes foi " , primeiraPrestacao)
