#l ()

#programa que mostre o menu abaixo, receba a opção do usuário e os dados necessários para executar a operação escolhida.

#Menu de opções:
#1 - Somar dois números
#2 - Dividir dois números
#3 - Raiz quadrada de um número
#Digite a opção desejada:

import math

print('Menu de opções:')
print('1 - Somar dois números')
print('2 - Dividir dois números')
print('3 - Raiz quadrada de um número')

opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 + num2
    print('A soma de %s e %.2f é %.2f.' % (num1, num2, resultado))
elif opcao == 2:
    num1 = float(input('Digite o dividendo: '))
    num2 = float(input('Digite o divisor: '))
    if num2 != 0:
        resultado = num1 / num2
        print('O resultado da divisão de %.2f por %.2f é %.2f.' % (num1, num2, resultado))
    else:
        print('Erro: Divisão por zero não é permitida.')
elif opcao == 3:
    num = float(input('Digite o número para calcular a raiz quadrada: '))
    if num >= 0:
        resultado = math.sqrt(num)
        print('A raiz quadrada de %.2f é %.2f.' % (num, resultado))
    else:
        print('Erro: Não é possível calcular a raiz quadrada de um número negativo.')
else:
    print('Opção inválida. Por favor, escolha uma opção entre 1 e 3.')