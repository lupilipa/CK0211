#l ()

#faça um programa que receba um número inteiro maior que 1, verifique se o número fornecido é primo ou não e mostre uma mensagem de número primo ou de número não primo.
#um número é primo quando é divisível apenas por 1 e por ele mesmo. 

print('Verificação de número primo')

numero = int(input('Digite um número inteiro maior que 1: '))

while numero <= 1:
    print('Número inválido! Digite um número maior que 1.')
    numero = int(input('Digite um número inteiro maior que 1: '))
    
eh_primo = True

for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')