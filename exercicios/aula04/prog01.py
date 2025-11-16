#l ()

"""
pseudocodigo:

algoritmo
    declare nota1, nota2, nota3, media_ponderada numerico
    escreva "Digite a primeira nota:"
    leia nota1
    escreva "Digite a segunda nota:"
    leia nota2
    escreva "Digite a terceira nota:"
    leia nota3
    media_ponderada <- (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)
    escreva "Média ponderada:", media_ponderada
    se media_ponderada >= 8 entao
        conceito <- 'A'
    senao se media_ponderada >= 7 entao
        conceito <- 'B'
    senao se media_ponderada >= 6 entao
        conceito <- 'C'
    senao se media_ponderada >= 5 entao
        conceito <- 'D'
    senao
        conceito <- 'E'
    fimse
    escreva "Conceito:", conceito
fim_algoritmo
"""

#receber três notas, calcular a média ponderada (peso 2, 3 e 5) e mostrar a média ponderada e o conceito correspondente (A, B, C, D ou E), sendo A entre 8 e 10, B entre 7 e 8, C entre 6 e 7, D entre 5 e 6 e E abaixo de 5

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)
print('Média ponderada:', media_ponderada)
if media_ponderada >= 8:
    conceito = 'A'
elif media_ponderada >= 7:
    conceito = 'B'
elif media_ponderada >= 6:
    conceito = 'C'
elif media_ponderada >= 5:
    conceito = 'D'
else:
    conceito = 'E'
print('Conceito:', conceito)