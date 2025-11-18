#l ()

#escreva um programa que peça para o usuário entrar com o número de linhas (m), colunas (n) e os elementos de uma matriz A e depois calcule e mostre a matriz B, tal que B é igual à transposta de A (AT)

"""
ALGORITMO 
    DECLARE A[100,100], B[100,100], m, n, i, j NUMÉRICO 
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
    PARA i ← 1 ATÉ m FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            B[j, i] ← A[i, j] 
        FIM 
    FIM 
    PARA i ← 1 ATÉ m FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            ESCREVA “B[“, i, “,”, j, “] = “, B[i,j] 
        FIM 
    FIM 
FIM_ALGORITMO
"""