#l ()

"""
pseudocodigo:

algoritmo
    declare n1, n2, n3 como numerico
    escreva "Digite o primeiro número:"
    leia n1
    escreva "Digite o segundo número:"
    leia n2
    escreva "Digite o terceiro número:"
    leia n3
    maior = n1
    se n2 > maior entao
        maior = n2
        menor = n1
    senao
        menor = n2
    fimse
    se n3 > maior entao
        meio = maior
        maior = n3
    senao
        se n3 < menor entao
            meio = menor
            menor = n3
        senao
            meio = n3
        fimse
    fimse
    escreva "Números em ordem crescente:", menor, ",", meio, ",", maior
fim_algoritmo
"""

#mostrar três números em ordem crescente; serão três números distintos

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = n1
if n2 > maior:
    maior = n2
    menor = n1
else:
    menor = n2
if n3 > maior:
    meio = maior
    maior = n3
else:
    if n3 < menor:
        meio = menor
        menor = n3
    else:
        meio = n3

print('Números em ordem crescente:', menor, ',', meio, ',', maior)