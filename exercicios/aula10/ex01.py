#l ()

#crie um programa que cria uma lista com 10 posições e peça para o usuário entrar com as 10 notas. as notas podem ser números reais

x = [0] * 10

for i in range(10):
    x[i] = float(input("digite a nota da %d ° posição: " % (i+1)))