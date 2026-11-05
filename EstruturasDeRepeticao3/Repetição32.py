nome = "a"
sexo = "a"
contagemHomem = 0
contagemMulher = 0
for contador in range (56):
    nome = input("Digite o seu nome ")
    sexo = input("Digite o seu sexo ")
    print  (nome , "-" , sexo)
    if sexo == "Masculino":
        contagemHomem += 1
    elif sexo == "Femenino":
        contagemMulher += 1
print ("Houveram " , contagemHomem , " homens e " , contagemMulher , " mulheres")
