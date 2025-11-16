#l ()

#faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado, seu cubo e sua raiz quadrada. 
#finalize a entrada de dados com um valor negativo ou zero.

print('Cálculo do quadrado, cubo e raiz quadrada de um número')

while True:
    numero = float(input('Digite um número (ou um valor negativo ou zero para sair): '))
    if numero <= 0:
        print('Programa finalizado.')
        break
    quadrado = numero ** 2
    cubo = numero ** 3
    raiz_quadrada = numero ** 0.5
    print(f'Número: {numero}, Quadrado: {quadrado}, Cubo: {cubo}, Raiz Quadrada: {raiz_quadrada}')