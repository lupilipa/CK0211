#l ()

#faça um programa que receba dez números inteiros, calcule e mostre a soma dos números pares e a soma dos números primos. um número é primo quando é divisível apenas por 1 e por ele mesmo. 

soma_pares = 0
soma_primos = 0

for i in range(10):
    num = int(input('digite o %sº número inteiro: ' % (i+1)))
    
    if num % 2 == 0:
        soma_pares += num
    
    if num > 1: 
        is_primo = True
        for j in range(2, int(num**0.5) + 1):
            ## verifica se o número é divisível por algum número entre 2 e a raiz quadrada de num
            if num % j == 0:
                is_primo = False
                break
        if is_primo:
            soma_primos += num
print('Soma dos números pares: {}'.format(soma_pares))
print('Soma dos números primos: {}'.format(soma_primos))

# outro jeito de usar números em strings