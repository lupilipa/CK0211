#l ()

#faça um programa que receba o valor de um empréstimo e mostre uma tabela com os seguintes dados: total a pagar, valor dos juros, quantidade de parcelas e valor da parcela. 
#os juros e a quantidade de parcelas seguem a tabela do topo. 
#um exemplo de saída para um empréstimo de R$1000,00 é mostrado na tabela ao lado

"""
Quantidade de parcelas - % de juros sobre o valor inicial do empréstimo
1 2
3 10
6 15
9 20
12 25

Total a pagar - Valor dos juros - Qtde de parcelas - Valor da parcela
R$1020,00 R$20,00 1 R$1020,00
R$1100,00 R$100,00 3 R$366,67
R$1150,00 R$150,00 6 R$191,67
"""

print('Calculadora de Empréstimos')

valor_emprestimo = float(input('Digite o valor do empréstimo (R$): '))

parcelas_juros = {
    1: 0.02,
    3: 0.10,
    6: 0.15,
    9: 0.20,
    12: 0.25
}

print('Total a pagar - Valor dos juros - Qtde de parcelas - Valor da parcela')

for parcelas, juros in parcelas_juros.items():
    valor_juros = valor_emprestimo * juros
    total_a_pagar = valor_emprestimo + valor_juros
    valor_parcela = total_a_pagar / parcelas
    print(f'R${total_a_pagar:.2f} R${valor_juros:.2f} {parcelas} R${valor_parcela:.2f}')