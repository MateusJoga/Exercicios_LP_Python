data = input('Informe data/mês/ano')
data = data.split('/')

if int(data[0]) < 1 or int(data[0]) > 31:
    print('O dia não é valido.')
if int()
elif int(data[1]) < 1 or int(data[1]) > 12:
    print('Não é um mês válido.')
elif int(data[2]) > 2025:
    print('Não é um ano válido.')
else:
    print('Data válida!')

for