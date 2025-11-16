#l ()

#faça um programa que mostre os primeiros 10 termos da sequência de Fibonacci: 0-1-1-2-3-5-8-13-21-34-…

print('Sequência de Fibonacci:')

termo1 = 0
termo2 = 1

print(termo1)
print(termo2)

for _ in range(8):
    proximo_termo = termo1 + termo2
    print(proximo_termo)
    termo1 = termo2
    termo2 = proximo_termo