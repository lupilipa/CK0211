#l ()

#média aritmética de duas notas e situação do aluno; aprovado sendo média maior ou igual a 7 e reprovado sendo média menor que 7

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Média:', media)
if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')