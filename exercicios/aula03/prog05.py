#l ()

"""
pseudocodigo:

algoritmo
    declare numero, quadrado, cubo, raiz_quadrada, raiz_cubica numerico
    escreva "Digite um número positivo: "
    leia numero
    se numero < 0 entao
        escreva "Número inválido! Por favor, digite um número positivo."
    senao
        quadrado <- numero * numero
        cubo <- numero * numero * numero
        raiz_quadrada <- raiz(numero)
        raiz_cubica <- numero^(1/3)
        escreva "Número: ", numero
        escreva "Ao quadrado: ", quadrado
        escreva "Ao cubo: ", cubo
        escreva "Raiz quadrada: ", raiz_quadrada
        escreva "Raiz cúbica: ", raiz_cubica
    fimse
fim_algoritmo
"""

#número positivo; ao quadrado, ao cubo, sua raiz quadrada e sua raiz cúbica

numero = float(input('Digite um número positivo: '))
if numero <= 0:
    print('Número inválido! Por favor, digite um número positivo.')
else:
    quadrado = numero ** 2
    cubo = numero ** 3
    raiz_quadrada = numero ** 0.5
    raiz_cubica = numero ** (1/3)
    print('Número:', numero)
    print('Ao quadrado:', quadrado)
    print('Ao cubo:', cubo)
    print('Raiz quadrada:', raiz_quadrada)
    print('Raiz cúbica:', raiz_cubica)