#l ()

#faça um programa que receba o número de alunos de uma turma, e para cada aluno receba duas notas, calcule e mostre:
#a média das duas notas, sabendo-se que a segunda nota possui peso 2;
#o resultado do aluno: Aprovado (se M ≥ 7), Reprovado (se M < 4) e AF (4 ≤ M < 7)
#ao final, mostre: Os totais de alunos aprovados, reprovados e que ficaram de AF e a média da turma. 
#Observação: se você já fez o programa media na última aula de laboratório, pode aproveitar parte do código.

num_alunos = int(input('Digite o número de alunos na turma: '))

total_aprovados = 0
total_reprovados = 0
total_af = 0
soma_medias = 0.0

for i in range(num_alunos):
    print(f'\nAluno {i + 1}:')
    ## \n para pular linha
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    media = (nota1 + 2 * nota2) / 3
    soma_medias += media

    print(f'Média do aluno: {media:.2f}')

    if media >= 7:
        print('Resultado: Aprovado')
        total_aprovados += 1
    elif media < 4:
        print('Resultado: Reprovado')
        total_reprovados += 1
    else:
        print('Resultado: AF')
        total_af += 1

media_turma = soma_medias / num_alunos
print('\nResumo da Turma:')
print(f'Total de alunos aprovados: {total_aprovados}')  
print(f'Total de alunos reprovados: {total_reprovados}')
print(f'Total de alunos de AF: {total_af}')
print(f'Média da turma: {media_turma:.2f}')