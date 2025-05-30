entrada = list(set(input('Digite um texto: ').split(' ')))

try:
    lista_int = [float(x) for x in entrada]
    print(sorted(lista_int, key=float ))

except:
    print(sorted(entrada, key=str))
