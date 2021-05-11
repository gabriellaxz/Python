a = int(input('entre com um valor: '))

div = 0
for x in range (1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print('número {} é primo'.format(a))
else:
    ('número {} não é primo'.format(a))

nota = float(input('Entre com a nota: '))
while nota > 10:
    nota = float(input('NOTA INVÁLIDA. Entre com a nota correta: '))
print(nota)