#l ()

#modifique o programa anterior tal que depois de receber as notas dos alunos, calcular a média da turma, e mostrar a posição na lista e a nota dos alunos que ficaram de AF (4 <= nota < 7)

x = [0] * 10
media = 0

for i in range(10):
    x[i] = float(input("digite a nota da %d ° posição: " % (i+1)))
    media += x[i]

print('a média da turma foi: %.2f' % (media/10))
print('alunos que ficaram de AF:')

for i in range(10):
    if x[i] >= 4 and x[i] < 7:
        print("nota do aluno %d: %.2f" % (i,x[i]))