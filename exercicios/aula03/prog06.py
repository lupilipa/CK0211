#l ()

"""
pseudocodigo:

algoritmo
    declare salario, percentual_aumento, valor_aumento, novo_salario numerico
    escreva "Digite o salário atual: "
    leia salario
    escreva "Digite o percentual de aumento: "
    leia percentual_aumento
    valor_aumento <- (salario * percentual_aumento) / 100
    novo_salario <- salario + valor_aumento
    escreva "O novo salário após o aumento é: ", novo_salario
fim_algoritmo
"""

#valor final de um salário após um aumento percentual

salario = float(input('Digite o salário atual: '))
percentual_aumento = float(input('Digite o percentual de aumento: '))
valor_aumento = (salario * percentual_aumento) / 100
novo_salario = salario + valor_aumento

print('Valor do aumento é:', valor_aumento)
print('O novo salário após o aumento é:', novo_salario)