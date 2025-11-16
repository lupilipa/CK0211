#l ()

"""
pseudocodigo:

algoritmo
    declare n1, n2, m, af, mf numerico
    escreva "Digite a primeira nota:"
    leia n1
    escreva "Digite a segunda nota:"
    leia n2
    m <- (n1 + n2) / 2
    se m >= 7 entao
        escreva "Aprovado com média:", m
    senao
        se m < 4 entao
            escreva "Reprovado com média:", m
        senao
            escreva "Aluno em AF com média:", m
            escreva "Digite a nota da AF:"
            leia af
            mf <- (m + af) / 2
            se mf >= 5 entao
                escreva "Aprovado na AF com média final:", mf
            senao
                escreva "Reprovado na AF com média final:", mf
            fimse
        fimse
    fimse
fim_algoritmo
"""

#calcular a média de duas notas; mostrar que m>=7 é aprovado, m<4 é reprovado, 4<=m<7 é af; se ficar af, receber a nota da af e calcular a média final entre m e a nota da af

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 7:
    print('Aprovado com média:', m)
else:
    if m < 4:
        print('Reprovado com média:', m)
    else:
        print('Aluno em AF com média:', m)
        af = float(input('Digite a nota da AF: '))
        mf = (m + af) / 2
        if mf >= 5:
            print('Aprovado na AF com média final:', mf)
        else:
            print('Reprovado na AF com média final:', mf)

