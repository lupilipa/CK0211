#l ()

#faça um programa que receba a idade de 8 pessoas, calcule e mostre:
#a) A quantidade de pessoas em cada faixa etária; 
#b) A porcentagem de pessoas na primeira faixa etária com relação ao total de pessoas
#c) A porcentagem de pessoas na última faixa etária com relação ao total de pessoas

"""
Faixa etária      Idade
1a                Até 15 anos
2a                De 16 a 30 anos
3a                De 31 a 45 anos
4a                De 46 a 60 anos
5a                Acima de 60 anos
"""

print('Faixa etária      Idade')
print('1a                Até 15 anos')
print('2a                De 16 a 30 anos')
print('3a                De 31 a 45 anos')
print('4a                De 46 a 60 anos')
print('5a                Acima de 60 anos')

faixa1 = 0
faixa2 = 0 
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range(8):
    idade = int(input('Digite a idade da pessoa {}: '.format(i+1)))
    if idade <= 15:
        faixa1 += 1
    elif 16 <= idade <= 30:
        faixa2 += 1
    elif 31 <= idade <= 45:
        faixa3 += 1
    elif 46 <= idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

total = 8

print('Quantidade de pessoas em cada faixa etária:')
print('1a faixa etária (Até 15 anos):', faixa1)
print('2a faixa etária (De 16 a 30 anos):', faixa2)
print('3a faixa etária (De 31 a 45 anos):', faixa3)
print('4a faixa etária (De 46 a 60 anos):', faixa4)
print('5a faixa etária (Acima de 60 anos):', faixa5)
print('Porcentagem de pessoas na 1a faixa etária: {:.2f}%'.format((faixa1 / total) * 100))
print('Porcentagem de pessoas na 5a faixa etária: {:.2f}%'.format((faixa5 / total) * 100))