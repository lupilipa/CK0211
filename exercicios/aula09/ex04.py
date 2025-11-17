#l ()

#faça um programa que receba o nome de um filme, o gênero ( 1- Ação, 2-Drama, 3-Comédia, 4 Animação), o valor do orçamento do filme (em milhões de dólares), o quanto o filme apurou nas bilheterias (em milhões de dólares) e calcule e mostre: 
#o lucro de cada filme em dólares; 
#a quantidade de filmes com lucro superior a 100 milhões de dólares; 
#o nome do filme mais lucrativo (nome e lucro); ignore empates; 
#o lucro médio dos filmes de Animação 
#ao final da entrada dos dados de cada filme, pergunte se o usuário deseja continuar a execução do programa: “Deseja continuar? (S/N): "

"""
Teste o seu programa com os seguintes filmes (valores em milhões de dólares)

Nome - Gênero - Orçamento (US$) - Bilheteria (US$)
Quem quer ser um milionário? Comédia 15 376
O Cisne Negro Drama 13 329
Shrek Terceiro Animação 160 799
O homem-aranha 3 Ação 258 891
Speed Racer Ação 120 94
Kung Fu Panda Animação 200 632
Encantada Comédia 85 340
Gran Torino Drama 33 270
"""

print('Catálogo de Filmes')

lucro_100 = 0
mais_lucrativo = " "
maior_lucro = 0
filme_animacao = 0
soma_animacao = 0
lucro_animacao = 0

while True:
    nome_filme = input('Informe o nome do filme: ')

    print('Qual o gênero do filme?: ')
    print('1 - Ação')
    print('2 - Drama')
    print('3 - Comédia')
    print('4 - Animação')

    genero_filme = input('Selecione o gênero: ')
    orcamento_filme = float(input('Informe o valor do orçamento do filme (em milhões de dólares): '))
    bilheteria_filme = float(input('Informe quanto o filme apurou nas bilheterias (em milhões de dólares): '))

    lucro = float(bilheteria_filme) - float(orcamento_filme)

    print('Esse filme teve um lucro de: ', lucro)

    if lucro > 100:
        lucro_100 += 1

    if lucro > maior_lucro:
        mais_lucrativo = nome_filme
        maior_lucro = lucro
    
    if genero_filme == "4":
        filme_animacao += 1
        soma_animacao = soma_animacao + lucro
        lucro_animacao = soma_animacao / filme_animacao

    continuar = input('Deseja continuar? (S/N): ')
    if continuar == 'N':
        break

print('Quantidade de filmes com lucro superior a 100 milhões de dólares: ', lucro_100, 'filmes')
print('Nome do filme mais lucrativo (nome e lucro): Nome: %s e Valor lucrado: %d milhões de dólares' % (mais_lucrativo, maior_lucro))
print('O lucro médio dos filmes de Animação: %d' % lucro_animacao, 'milhões de dólares')