#l ()

#Jogo: adivinhe o número professional 
#modifique o programa do jogo anterior, tal que agora você mostre uma lista de níveis para o jogador escolher, como mostrado a seguir;
#o nível Beginner é o mesmo programa anterior; 
#o nível hard limita o número de tentativas em 3, ainda mostrando as dicas; 
#o nível insane também limita o número de tentativas em 3, mas sem dicas.

#Adivinhe o número! Escolha o nível
#1 - Beginner
#2 - Hard
#3 - Insane
#Digite a sua opção:

import random
n = random.randint(1,10)
tentativas = 0

print("Adivinhe o número! Escolha o nível")
print("1 - Beginner")
print("2 - Hard")
print("3 - Insane")

nivel = int(input("Digite a sua opção: "))

if nivel == 1:
    while True:
        palpite = int(input('Digite seu palpite (número entre 1 e 10): '))
        tentativas += 1
        if palpite < n:
            print('Tente um número maior.')
        elif palpite > n:
            print('Tente um número menor.')
        else:
            print(f'Parabéns! Você acertou o número {n} em {tentativas} tentativas.')
            break
elif nivel == 2:
    while tentativas < 3:
        palpite = int(input('Digite seu palpite (número entre 1 e 10): '))
        tentativas += 1
        if palpite < n:
            print('Tente um número maior.')
        elif palpite > n:
            print('Tente um número menor.')
        else:
            print(f'Parabéns! Você acertou o número {n} em {tentativas} tentativas.')
            break
    else:
        print(f'Você esgotou suas tentativas! O número era {n}.')
elif nivel == 3:
    while tentativas < 3:
        palpite = int(input('Digite seu palpite (número entre 1 e 10): '))
        tentativas += 1
        if palpite == n:
            print(f'Parabéns! Você acertou o número {n} em {tentativas} tentativas.')
            break
    else:
        print(f'Você esgotou suas tentativas! O número era {n}.')
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")