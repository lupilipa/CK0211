#l ()

#faça uma função (cria_matriz) que cria uma matriz m por n, preenchida com zeros e uma função (print_matriz) que mostra uma matriz de qualquer dimensão 
#crie um programa que utiliza a função cria_matriz para criar uma matriz 4 por 3 e usa a função print_matriz para mostrar os seus valores na tela

def cria_matriz(m, n): 
    mat = [] 
    for i in range(m): 
        linha = [0] * n 
        mat.append(linha) 
    return mat 
def print_matriz(mat): 
    for linha in mat: 
        for elemento in linha: 
            print("%8.2f" % elemento, end=" ") 
        print("") 
M = cria_matriz(4,3) 
print_matriz(M)