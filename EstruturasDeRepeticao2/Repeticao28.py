preco = int(input("Escreva o preço do carro "))
precoFinal = 0
parcelas = 0
valorParcela = 0
print ("|            O preço à vista é " , ((preco * 80) / 100) , "                      |\n|Preço final    Quantidade de parcelas    Valor da parcela|")
for contador in range (10):
    parcelas += 6
    precoFinal = (preco * ((parcelas / 2) + 100)) / 100
    valorParcela = precoFinal / parcelas
    print ("|" , precoFinal , "              " , parcelas , "              " , valorParcela , "|")