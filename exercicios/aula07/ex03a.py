#l ()

#na última aula vimos o algoritmo para calcular o fatorial de um número inteiro positivo digitado pelo usuário. certifique-se de que o número é mesmo maior que 0.

#Digite um número inteiro positivo: 4
#Fatorial de 4: 24

"""
algoritmo
    declare num, fatorial numerico
    escreva "digite um número maior que zero: "
    leia num
    se num <= 0 então
        escreva "inválido! digite um número maior que zero: "
        leia num
    fatorial <- 1
    para i <- num até 1 faça
        início
            fatorial <- fatorial * num
            num <- num - 1
        fim
    escreva "o fatorial de ", num, " é ", fatorial
fim_algoritmo
"""

"""
- entrada de dados:
num = inteiro (maior que 0)

- processamentos:
num = int(input('digite um número inteiro positivo: '))

if num <= 0:
    while num <= 0:
        num = int(input('inválido! digite um número maior que zero: '))

fatorial = 1
j = num
for i in range(j, 0, -1):
    fatorial = fatorial * j
    j -= 1
print('o fatorial de', num, 'é', fatorial)

## só atribuir o valor qu não pode ser mudado, para uma nova variável

- saída de dados:
fatorial = inteiro
"""

num = int(input('digite um número inteiro positivo: '))

if num <= 0:
    while num <= 0:
        num = int(input('inválido! digite um número maior que zero: '))

fatorial = 1
j = num
for i in range(j, 0, -1):
    fatorial = fatorial * j
    j -= 1
print('o fatorial de', num, 'é', fatorial)