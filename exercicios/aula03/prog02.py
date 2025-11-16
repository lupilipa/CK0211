#l ()

"""
pseudocodigo:

algoritmo
    declare nota1, nota2, nota3, media numerico
    escreva "Digite a primeira nota: "
    leia nota1
    escreva "Digite a segunda nota: "
    leia nota2
    escreva "Digite a terceira nota: "
    leia nota3
    media <- (nota1 + nota2 + nota3) / 3
    escreva "A média das três notas é: ", media
fim_algoritmo
"""

#média de três notas

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média das três notas é:', media)