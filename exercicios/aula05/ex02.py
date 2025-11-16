#l ()

#codifique o fluxograma em Python e diga o resultado se o dado de entrada for sua idade

i = int(input('Digite um número: '))
if i%2 == 0:
    i += 10
else:
    i *= 2
print('resultado: %d' % i)

#resultado: se a idade for par, soma 10; se for ímpar, multiplica por 2