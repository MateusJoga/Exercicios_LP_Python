quant = int(input(''))

while quant != 0:
    a = int(input(''))
    b = int(input(''))
    if a > b:
        maior = a
    elif b > a:
        maior = b
    while a % maior != b % maior:
        maior -= 1


    print(f'{maior}')
    quant -= 1