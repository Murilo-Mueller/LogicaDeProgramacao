import random
pecas = int(input("Escreva quantas peças serão feitas "))
meta = int(input("Digite a meta "))
maximo = int(input("Digite o máximo de peças que uma máquina aguenta fazer "))
estado = "Meta não atingida"
estadoMaquina = "A máquina não quebrou"
acumulo = 0
contador = 0
aleatorio = 0
somaPecas = 0
for contadorParaOFor in range (5):
    if somaPecas >= meta:
        estado = "Meta diária atingida"
        break
    else:
        acumulo = maximo - pecas
        contador += 1
    if acumulo > ((maximo * 90) / 100):
        aleatorio = random.randint(1,2)
        if aleatorio == 1:
            estadoMaquina = "A máquina quebrou"
    somaPecas += pecas
if somaPecas >= meta:
    estado = "Meta diária atingida"
elif acumulo >= meta:
    estado = "Falha estrutural"
print (somaPecas , " peça(s) foram produzidas\n" , estado , "\n" , contador , "ciclos executados")
