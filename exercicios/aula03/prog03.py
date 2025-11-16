#l ()

"""
pseudocodigo:

algoritmo
    declare nota1, peso1, nota2, peso2, media_ponderada numerico
    escreva "Digite a primeira nota: "
    leia nota1
    escreva "Digite o peso da primeira nota: "
    leia peso1
    escreva "Digite a segunda nota: "
    leia nota2
    escreva "Digite o peso da segunda nota: "
    leia peso2
    media_ponderada <- (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    escreva "A média ponderada das duas notas é: ", media_ponderada
fim_algoritmo
"""

#média ponderada de duas notas

nota1 = float(input('Digite a primeira nota: '))
peso1 = float(input('Digite o peso da primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
peso2 = float(input('Digite o peso da segunda nota: '))

media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print('A média ponderada das duas notas é:', media_ponderada)