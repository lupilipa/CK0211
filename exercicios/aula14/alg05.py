#l ()

#escreva um programa que multiplica duas matrizes A e B. 
#verifique se as matrizes podem ser multiplicadas antes de realizar a multiplicação, mostrando uma mensagem de erro se não for possível

"""
ALGORITMO 
    DECLARE A[100,100], B[100,100], C[100,100], m, n, NUMÉRICO 
            mB, s, i, j, k NUMÉRICO 
    ESCREVA “Digite o número de linhas de A (máx. 100)” 
    LEIA m 
    ESCREVA “Digite o número de colunas de A (máx. 100)” 
    LEIA n 
    ESCREVA “Digite o número de linhas de B (máx. 100)” 
    LEIA mB 
    SE mb ≠ n ENTÃO 
    INÍCIO 
        ESCREVA “Número de linhas de B ≠ número de colunas de A” 
    FIM 
    SENÃO 
    INÍCIO 
        ESCREVA “Digite o número de colunas de B (máx. 100)” 
        LEIA p
    FIM
    PARA i ← 1 ATÉ m FAÇA 
    INÍCIO 
        PARA k ← 1 ATÉ p FAÇA 
        INÍCIO 
            s ← 0 
            PARA j ← 1 ATÉ n FAÇA 
            INÍCIO 
                s ← s + A[i,j] * B[j,k] 
            FIM 
            C[i,k] ← s
        FIM
    FIM 
FIM
"""