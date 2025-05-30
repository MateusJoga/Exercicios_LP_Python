lista = []
maior = 0
contador = 0

for i in range(0,100):
    lista.append(int(input()))

for i in lista:
    contador +=1
    if i > maior:
        maior = i
        lugar = contador

print(maior)
print(lugar)

