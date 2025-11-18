#l ()

#modifique o programa anterior de modo a mostrar as notas digitadas ao final do programa (tente usar os dois modos)

x = [0] * 10

for i in range(10):
    x[i] = float(input("digite a nota da %d ° posição: " % (i+1)))

for i in range(10):
    print(x[i])