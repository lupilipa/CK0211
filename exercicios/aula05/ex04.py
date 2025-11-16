#l ()

#programa que recebe três valores A, B e C, e informe se eles podem ser os lados de um triângulo. o ABC é um triângulo se, e somente se, cada lado for menor que a soma dos outros dois lados.

A = float(input('Digite o valor do lado A: '))
B = float(input('Digite o valor do lado B: '))
C = float(input('Digite o valor do lado C: '))

if A < B + C and B < A + C and C < A + B:
    print('Os valores podem ser os lados de um triângulo.')
else:
    print('Os valores não podem ser os lados de um triângulo.')