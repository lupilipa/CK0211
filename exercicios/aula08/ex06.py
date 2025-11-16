#l ()

#cada espectador de um cinema respondeu a um questionário no qual constava  sua idade e sua opinião em relação ao filme: ótimo - 3; bom - 2; regular - 1. 
#faça um programa que receba a idade e a opinião de 15 espectadores, calcule e mostre: 
#a média das idades das pessoas que responderam ótimo; 
#a quantidade de pessoas que responderam regular; 
#e a percentagem de pessoas que responderam bom, entre todos os espectadores analisados

print('Responda a pesquisa sobre o filme:')
print('Opiniões: ótimo - 3; bom - 2; regular - 1')

soma_idade_otimo = 0
quantidade_otimo = 0
quantidade_regular = 0
quantidade_bom = 0

for i in range(15):
    idade = int(input(f'Digite a idade do espectador {i+1}: '))
    opiniao = int(input(f'Digite a opinião do espectador {i+1} (3-ótimo, 2-bom, 1-regular): '))
    
    if opiniao == 3:
        soma_idade_otimo += idade
        quantidade_otimo += 1
    elif opiniao == 2:
        quantidade_bom += 1
    elif opiniao == 1:
        quantidade_regular += 1

if quantidade_otimo > 0:
    media_idade_otimo = soma_idade_otimo / quantidade_otimo
    print(f'Média das idades das pessoas que responderam ótimo: {media_idade_otimo:.2f}')
else:
    print('Nenhum espectador respondeu ótimo.')

print(f'Quantidade de pessoas que responderam regular: {quantidade_regular}')

percentagem_bom = (quantidade_bom / 15) * 100

print(f'Percentagem de pessoas que responderam bom: {percentagem_bom:.2f}%')