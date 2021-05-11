a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or not resto_b > 0:
    print('foi digitado um número par')
else:
    print('nenhum número par foi digitado')

#notasbimestrais
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre:'))
media = (a + b + c + d) /4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {} '.format(media))
else:
    print('foi informado alguma nota errada')