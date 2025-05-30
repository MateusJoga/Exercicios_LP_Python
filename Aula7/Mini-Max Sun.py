numeros = str(input('Digite 5 numeros inteiros positivos: ')).split(' ')
total = 0
print(numeros)

for i in numeros:
    i = int(i)
    maior = 0
    menor = int(numeros[0])
    total += i

    if i > maior:
        maior = i
    
    if i < menor:
        menor = i

print(f'{total - maior} {total - menor}')