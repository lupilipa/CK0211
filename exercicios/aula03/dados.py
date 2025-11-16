#l ()

#entrada de dados = input

nome = input('qual o seu nome? ')
idade = input('qual a sua idade? ')
print(type(idade)) # <class 'str'>

nome = input('qual o seu nome? ')
idade = int(input('qual a sua idade? '))
print(type(idade)) # <class 'int'>

#saida de dados = print

print('olá', nome, 'sua idade é', idade)