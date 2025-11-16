#l ()

#modifique o seu programa, tal que o programa possa calcular o fatorial de vários números em uma mesma execução. o usuário deve digitar um número menor ou igual a zero para interromper a execução.
#dica: você vai precisar de dois laços aninhados para implementar esse programa. um exemplo de execução do programa é mostrado a seguir:

#Digite um número inteiro positivo: 4
#Fatorial de 4: 24
#Digite um número inteiro positivo: 5
#Fatorial de 4: 120
#Digite um número inteiro positivo: 0
#Fim.

"""
- entrada de dados:
num = inteiro (maior que 0)
ou num <= 0 para sair

- processamentos:
num = int(input('digite um número inteiro positivo: '))

if num <= 0:
    print('fim.')
else:
    while True:
        fatorial = 1
        j = num
        for i in range(j, 0, -1):
            fatorial = fatorial * j
            j -= 1
        print('o fatorial de', num, 'é', fatorial)
        num = int(input('digite um número inteiro positivo: '))
        if num <= 0:
            break
    print('fim.')

- saída de dados:
fatorial = inteiro
"""

num = int(input('digite um número inteiro positivo: '))

if num <= 0:
    print('fim.')
else:
    while True:
        fatorial = 1
        j = num
        for i in range(j, 0, -1):
            fatorial = fatorial * j
            j -= 1
        print('o fatorial de', num, 'é', fatorial)
        num = int(input('digite um número inteiro positivo: '))
        if num <= 0:
            break
    print('fim.')