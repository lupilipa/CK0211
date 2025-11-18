#l ()

#escreva um programa que crie e mostre uma matriz identidade de ordem n entrada pelo usuário

"""
ALGORITMO 
    DECLARE I[100,100], n, i, j NUMÉRICO 
    ESCREVA “Digite a ordem da matriz identidade a ser criada (máx. 100)” 
    LEIA n 
    PARA i ← 1 ATÉ n FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            SE i = j ENTÃO I[i,j] ← 1 
            SENÃO I[i,j] ← 0 
        FIM 
    FIM 
    PARA i ← 1 ATÉ n FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            ESCREVA “I[“, i, “,”, j, “] = “, I[i,j] 
        FIM 
    FIM 
FIM_ALGORITMO
"""