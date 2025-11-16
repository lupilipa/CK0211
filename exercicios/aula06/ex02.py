#l ()

#usando for; mostrar tabuada d um número maior que zero e inteiro, <=10

num = int(input('digite um número inteiro maior que zero e menor ou igual a 10: '))

if num > 0 and num <= 10:
    print('Tabuada do %d:' % num)
    for i in range(1, 11):
        resultado = num * i
        print('%d x %d = %d' % (num, i, resultado))
else:
    print('número incorreto')