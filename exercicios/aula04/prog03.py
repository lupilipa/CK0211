#l ()

"""
pseudocodigo:

algoritmo
    declare a, b numerico
    escreva "Digite o primeiro número:"
    leia a
    escreva "Digite o segundo número:"
    leia b
    se a > b entao
        escreva "O maior número é:", a
    senao
        escreva "O maior número é:", b
    fimse
fim_algoritmo
"""

#mostrar o maior entre dois números

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

if a > b:
    print('O maior número é:', a)
else:
    print('O maior número é:', b)