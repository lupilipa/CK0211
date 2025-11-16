#l ()

#programa que pede os dados valor do salario e percentual de aumento; depois mostre o valor do aumento e o novo salario com duas casas decimais

#saída: digite o salario atual:
#entrada: 1000.00
#saída: digite o percentual de aumento:
#entrada: 15
#saída: o valor do aumento é: 150.00
#saída: o novo salario é: 1150.00

salario_atual = float(input('Digite o salário atual: '))
percentual_aumento = float(input('Digite o percentual de aumento: '))
valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

print('o valor do aumento é: %.2f' % valor_aumento)
print('o novo salário é: %.2f' % novo_salario)