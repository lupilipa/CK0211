#l ()

#um funcionário de uma empresa recebe aumento salarial anualmente. sabe-se que:
#- o funcionário que ingressou na empresa em 2005, com o salário inicial de R$ 1.000,00; em 2006 ele recebeu aumento de 1,5% sobre o salário inicial; a partir de 2007, os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#- faça um programa que determine o salário atual desse funcionário.

"""
algoritmo
    declare i, ano_atual, salario, percentual numérico
    leia ano_atual
    salario <- 1000.00
    percentual <- 1.5/100
    salario <- salario + percentual * salario
    para i <- 2007 até ano_atual faça
    início
        percentual <- 2 * percentual
        salario <- salario + percentual * salario
    fim
    escreva salario
fim_algoritmo
"""

#implemente com for em python; depois implemente com while; depois teste com 2016 o ano atual

ano_atual = int(input('Digite o ano atual: '))
salario = 1000.00
percentual = 1.5 / 100
salario = salario + percentual * salario

for i in range(2007, ano_atual + 1):
    percentual = 2 * percentual
    salario = salario + percentual * salario
print('Salário atual: R$ %.2f' % salario)

ano_atual = int(input('Digite o ano atual: '))
salario = 1000.00
percentual = 1.5 / 100
salario = salario + percentual * salario

i = 2007
while i <= ano_atual:
    percentual = 2 * percentual
    salario = salario + percentual * salario
    i += 1
print('Salário atual: R$ %.2f' % salario)