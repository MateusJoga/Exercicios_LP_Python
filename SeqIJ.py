i = 0
j = 1
contador = 0
print(f'I={i} J={j}')

while i != 2:
    contador += 1
    j += 1
    print(f'I={i} J={j}')
    if contador == 2:
        i += 0.2
        j = (j + 0.2) - 2
        contador = 0
        print(f'I={i} J={j}')
    