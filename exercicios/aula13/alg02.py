#l ()

#faça um programa que preencha uma matriz 2 x 2 , calcule e mostre a matriz R, resultante da multiplicação dos elementos de M pelo seu maior elemento

"""
ALGORITMO 
    DECLARE M[2,2], R[2,2], i, j, maior NUMÉRICO  
    PARA i ← 1 ATÉ 2 FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ 2 FAÇA 
        INÍCIO 
            LEIA M[i,j] 
        FIM 
    FIM 
    maior ← M[1,1] 
    PARA i ← 1 ATÉ 2 FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ 2 FAÇA 
        INÍCIO 
            SE M[i,j] > maior ENTÃO maior ← M[i,j] 
        FIM 
    FIM 
    PARA i ← 1 ATÉ 2 FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ 2 FAÇA 
        INÍCIO 
            R[i,j] ← maior * M[i,j] 
        FIM 
    FIM 
    PARA i ← 1 ATÉ 2 FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ 2 FAÇA 
        INÍCIO 
            ESCREVA R[i,j] 
        FIM 
    FIM 
FIM_ALGORITMO
"""

M = [[0,0],[0,0]] 
for i in range(2): 
    for j in range(2): 
        M[i][j] = float(input("Digite um número: "))  
maior = M[0][0] 
for i in range(2): 
    for j in range(2): 
        if M[i][j] > maior: 
            maior = M[i][j] 
R = [[0,0],[0,0]] 
for i in range(2): 
    for j in range(2): 
        R[i][j] = maior * M[i][j] 
for i in range(2): 
    for j in range(2): 
        print(R[i][j])