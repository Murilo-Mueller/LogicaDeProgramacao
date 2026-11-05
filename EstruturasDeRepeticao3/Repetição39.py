codigo = 0
salario = 0
funcionario1 = 0 #admnistrativo
funcionario2 = 0 #empresarial
soma1 = 0
soma2 = 0
for contador in range (20) :
    codigo = int(input("Digite o seu código "))
    salario = int(input("Digite o seu salário "))
    if codigo == 1:
        soma1 += salario
        funcionario1 += 1
    else:
        soma2 += salario
        funcionario2 += 1
print ("A média salarial do setor administrativo é de " , (soma1 / 20) , ". A média salarial do setor empresarial é de " , (soma2 / 20) , ". O total de salários pagos pela empresa é de 20. A quantidade de funcionários do setor administrativo é de " , funcionario1 , " e a quantidade de funcionários do setor empresarial é de " , funcionario2)
    