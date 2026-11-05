codigo = 1
quantidade = 0
valor = 0
valorTotal = 0
preco = 0
print ("|Especificação      Código     Preço|")
print ("|Cachorro Quente     100     R$ 1,20|")
print ("|Bauru Simples       101     R$ 1,30|")
print ("|Bauru com ovo       102     R$ 1,50|")
print ("|Hambúrguer          103     R$ 1,20|")
print ("|Cheeseburguer       104     R$ 1,30|")
print ("|Refrigerante        105     R$ 1,00|")
print ("|  Digite 0 para encerrar o pedido  |")
while True:
    codigo = int(input("Escreva o código da comida "))
    if codigo == 0:
        break
    elif codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1
    else:
        print ("Esse código não é compatível ")
    quantidade = int(input("Escreva a quantidade que você quer pedir "))
    valor = preco * quantidade
    valorTotal += valor
    print ("O valor do pedido é " , valor , " e o valor total é " , valorTotal)