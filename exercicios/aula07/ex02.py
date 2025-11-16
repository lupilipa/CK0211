#l ()

#uma pessoa gostaria de fazer uma viagem que custa uma quantia V em reais e precisa de ajuda com o planejamento. a pessoa está disposta a fazer uma poupança iniciando em I reais e irá depositar mensalmente uma quantia M na poupança. 
#sabendo que a poupança rende 0,5% ao mês, faça um programa que receba esses dados do usuário e estime em quantos meses ele conseguiria o dinheiro para viajar. 

"""
- entrada de dados:
valor_viagem = valor em reais da viagem
valor_inicial = valor inicial
deposito_mensal = valor depositado mensalmente

- processamento:
valor_viagem = float(input('valor da viagem: '))
valor_inicial = float(input('valor inicial: '))
deposito_mensal = float(input('depósito mensal: '))

meses = 0
poupanca = valor_inicial
aumento = 0.5 / 100

while True:
    poupanca = poupanca + (poupanca * aumento) + deposito_mensal
    meses += 1
    if poupanca >= valor_viagem:
        break
print('meses necessários:', meses)
        
- saída de dados:
número de meses = ?
"""

valor_viagem = float(input('valor da viagem: '))
valor_inicial = float(input('valor inicial: '))
deposito_mensal = float(input('depósito mensal: '))

meses = 0
poupanca = valor_inicial
aumento = 0.5 / 100

while True:
    poupanca = poupanca + (poupanca * aumento) + deposito_mensal
    meses += 1
    if poupanca >= valor_viagem:
        break
print('meses necessários:', meses)