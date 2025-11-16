#l ()

#faça um programa para calcular a área de um triângulo, recebendo a base e altura e que não permita a entrada de dados inválidos (valores menores ou iguais a 0). 

print('Cálculo da área de um triângulo')

base = float(input('Digite o valor da base: '))

while base <= 0:
    print('Valor inválido! A base deve ser maior que 0.')
    base = float(input('Digite o valor da base: '))

altura = float(input('Digite o valor da altura: '))

while altura <= 0:
    print('Valor inválido! A altura deve ser maior que 0.')
    altura = float(input('Digite o valor da altura: '))
    
area = (base * altura) / 2

print(f'A área do triângulo é: {area}')