lista = []
entrada = ''

while entrada != 'SAIR':
    entrada = input('Digite um número. (DIGITE *SAIR*)')

    try:
        entrada = int(entrada)
        lista.append(entrada)
    except:
        continue

lista = sorted(lista)
print(lista)
print(f'{lista[0] + lista[1] + lista[2]} {lista[-1] + lista[-2] + lista[-3]}')
