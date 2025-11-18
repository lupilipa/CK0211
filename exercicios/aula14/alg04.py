#l ()

#crie um programa que preencha uma matriz A, m x n (m e n entrados pelo usuário) e um vetor v de tamanho n e calcule e mostre o produto de A por v

"""
ALGORITMO 
    DECLARE A[100,100], R[100], v[100], m, n, s, i, j NUMÉRICO 
    ESCREVA “Digite o número de linhas de A (máx. 100)” 
    LEIA m 
    ESCREVA “Digite o número de colunas de A (máx. 100)” 
    LEIA n 
    PARA i ← 1 ATÉ m FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            LEIA A[i, j] 
        FIM 
    FIM 
    PARA i ← 1 ATÉ n FAÇA 
    INÍCIO 
        LEIA v[i] 
    FIM
    PARA i ← 1 ATÉ m FAÇA 
    INÍCIO 
        s ← 0 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            s ← s + A[i, j] * v[j] 
        FIM 
        R[i] ← s 
    FIM 
    PARA i ← 1 ATÉ m FAÇA 
    INÍCIO 
        ESCREVA “R[“, i, “] = “, R[i] 
    FIM 
FIM_ALGORITMO
"""