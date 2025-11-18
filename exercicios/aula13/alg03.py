#l ()

#faça um programa que preencha uma matriz 5 x 3  com as notas de 5 alunos em três provas. 
#o programa deverá mostrar um relatório com o número dos 5 alunos e a prova em que cada aluno obteve menor nota. 
#ao final do relatório, deverá mostrar quantos alunos tiveram menor nota em cada uma das provas: na prova 1, na prova 2, na prova 3

"""
ALGORITMO 
    DECLARE notas[5,3], i, j, menor, menor_p, q1, q2, q3 NUMÉRICO  
    PARA i ← 1 ATÉ 5 FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ 3 FAÇA 
        INÍCIO 
            LEIA notas[i,j] 
        FIM 
    FIM 
    q1 ← 0 
    q2 ← 0 
    q3 ← 0
    PARA i ← 1 ATÉ 5 FAÇA 
    INÍCIO 
        ESCREVA i 
        menor ← notas[i,1] 
        menor_p ← 1 
        PARA j ← 1 ATÉ 3 FAÇA 
        INÍCIO 
            SE notas[i,j] < menor ENTÃO 
            INÍCIO 
                menor ← notas[i,1] 
                menor_p ← j 
            FIM  
        FIM 
        ESCREVA p_menor 
        SE menor_p = 1 ENTÃO q1 ← q1 + 1 
        SE menor_p = 2 ENTÃO q2 ← q2 + 1 
        SE menor_p = 3 ENTÃO q3 ← q3 + 1 
    FIM 
    ESCREVA q1, q2, q3 
FIM_ALGORITMO
"""

notas = [] 
for i in range(5): 
    linha = [0] * 3 
    notas.append(linha) 
for i in range(5): 
    for j in range(3): 
        notas[i][j] = float(input("Digite a nota %d do aluno %d: "% (j+1,i+1)))  
q1 = 0 
q2 = 0 
q3 = 0 
for i in range(5): 
    menor = notas[i][0] 
    menor_p = 0 
    for j in range(3): 
        if notas[i][j] < menor: 
            menor = notas[i][j] 
            menor_p = j 
    print(i, menor_p) 
    if menor_p == 0: 
        q1 += 1 
    if menor_p == 1: 
        q2 += 1 
    if menor_p == 2: 
        q3 += 1 
print(q1, q2, q3)