#l ()

#faça um programa que receba dez números inteiros e mostre a quantidade de números primos dentre os números que foram digitados

print('Contador de números primos')

quantidade_primos = 0

for _ in range(10):
    numero = int(input('Digite um número inteiro: '))
    if numero > 1:
        eh_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break
        if eh_primo:
            quantidade_primos += 1
            
print(f'Quantidade de números primos digitados: {quantidade_primos}')