#l ()

#mesmo código da aula anterior, mas usando formatação de strings

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 7:
    print('Aprovado com média: %f' % m)
else:
    if m < 4:
        print('Reprovado com média: %f' % m)
    else:
        print('Aluno em AF com média: %.2f' % m)
        af = float(input('Digite a nota da AF: '))
        mf = (m + af) / 2
        if mf >= 5:
            print('Aprovado na AF com média final: %d' % mf)
        else:
            print('Reprovado na AF com média final: %d' % mf)
