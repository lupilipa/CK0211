#l ()

#Jogo: adivinhe o número amador 
#faça um programa que escolha um número aleatório entre 1 e 10 e peça para o usuário adivinhá-lo. 
#permita tantas tentativas quanto forem necessárias para o usuário acertar o número. mostre dicas ao usuário, quando ele errar: tente um número maior ou tente um número menor. 
#ao final diga em quantas tentativas o usuário acertou o número. 
#para a escolha do número aleatório entre x e y, use a função randint(x,y) da biblioteca random, como mostrado a seguir:

#import random #biblioteca para números aleatórios
#escolher um número inteiro de 1 a 10
#n = random.randint(1,10)

import random
n = random.randint(1,10)
tentativas = 0

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