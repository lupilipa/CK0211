#l ()

#receber três números inteiros e informar o maior número ímpar entre eles. caso nenhum número ímpar seja digitado, deve ser exibida uma mensagem informando isso.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1%2 != 0 or num2%2 != 0 or num3%2 != 0:
    maior_impar = 0
    if num1%2 != 0:
        maior_impar = num1
    if num2%2 != 0 and num2 > maior_impar:
        maior_impar = num2
    if num3%2 != 0 and num3 > maior_impar:
        maior_impar = num3
    print(f'O maior número ímpar digitado foi: %d' % maior_impar)
else:
    print('Nenhum número ímpar foi digitado.')