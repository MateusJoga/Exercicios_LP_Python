quant = 0

while quant < 15:
    nota = int(input('Digite uma nota: '))
    if nota >= 0 and nota <= 5:
        quant += 1
        print(f'{quant}° Nota válida: {nota}')
    else:
        print('Nota inválida. Tente novamente.')