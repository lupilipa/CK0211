#l ()

#escreva um programa que dada uma matriz quadrada Q, calcule o traço(Q). 
#o traço de uma matriz é a soma dos elementos da diagonal principal

"""
ALGORITMO 
    DECLARE Q[100,100], n, i, j, tr NUMÉRICO 
    ESCREVA “Digite a ordem da matriz Q (máx. 100)” 
    LEIA n 
    PARA i ← 1 ATÉ n FAÇA 
    INÍCIO 
        PARA j ← 1 ATÉ n FAÇA 
        INÍCIO 
            LEIA Q[i, j] 
        FIM 
    FIM 
    tr ← 0 
    PARA i ← 1 ATÉ n FAÇA 
    INÍCIO 
        tr ← tr + Q[i, i] 
    FIM 
    ESCREVA “tr(Q) = “, tr 
FIM_ALGORITMO
"""