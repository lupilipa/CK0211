#l ()

#faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. 
#finalize digitando idade igual a 0. 
#números negativos não são aceitos; mostre uma mensagem de idade inválida, mas não interrompa o programa

print('Cálculo da média das idades')

soma_idades = 0
quantidade_idades = 0

while True:
    idade = int(input('Digite uma idade (ou 0 para finalizar): '))
    if idade < 0:
        print('Idade inválida! Digite uma idade maior ou igual a 0.')
        continue
    if idade == 0:
        break
    soma_idades += idade
    quantidade_idades += 1
    
if quantidade_idades > 0:
    media_idades = soma_idades / quantidade_idades
    print(f'Média das idades digitadas: {media_idades:.2f}')
else:
    print('Nenhuma idade válida foi digitada.')