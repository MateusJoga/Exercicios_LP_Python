entrada = str(input('Digite uma frase: ').split(' '))
lista_letra = []

for palavra in entrada:
    trans = palavra.split()
    for letra in trans:
        if letra.isalpha() == True:
            minusculo = letra.lower()
            print(minusculo)
            lista_letra.append(str(minusculo))
        else:
            continue

print(sorted(set(lista_letra), key=str))
