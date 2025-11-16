#l ()

"""
pseudocodigo:

algoritmo
    declare matricula, idade numerico
            nome, curso, email caractere
    escreva "Digite sua matrícula: "
    leia matricula
    escreva "Digite seu nome: "
    leia nome
    escreva "Digite sua idade: "
    leia idade
    escreva "Digite seu curso: "
    leia curso
    escreva "Digite seu email: "
    leia email
    escreva "Ficha de Inscrição:"
    escreva "Matrícula: ", matricula
    escreva "Nome: ", nome
    escreva "Idade: ", idade
    escreva "Curso: ", curso
    escreva "Email: ", email
fim_algoritmo
"""

#ficha de inscrição

matricula = int(input('Digite sua matrícula: '))
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
curso = input('Digite seu curso: ')
email = input('Digite seu email: ')

print('Ficha de Inscrição:')
print('Matrícula:', matricula)
print('Nome:', nome)
print('Idade:', idade)
print('Curso:', curso)
print('Email:', email)