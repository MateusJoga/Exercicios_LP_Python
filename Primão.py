numero = int(input('Digite um numero: '))
lista = []
contador = 1

while contador < numero:
    ePrimo = False
    contador +=1
    primo = 1

    while contador > primo:
        primo += 1
        if contador % primo == 0 and not contador == primo:
            ePrimo = True

    if ePrimo == False:
        lista.append(contador)

print(lista)