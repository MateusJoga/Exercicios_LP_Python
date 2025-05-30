Num = int(input())
lista = []
cobaia = 0
rato = 0
coelho = 0
sapo = 0
total = 0

for i in range(0,Num):
    entrada = input()
    lista = entrada.split(' ')
    if lista[1] == 'C':
        coelho += int(lista[0])
    elif lista[1] == 'R':
        rato += int(lista[0])
    elif lista[1] == 'S':
        sapo += int(lista[0])
    else:
        print('Entrada inválida')
    cobaia += int(lista[0])

print(f'Total: {cobaia} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}\nPercentual de coelhos: {(coelho/cobaia)*100:.2f} %\nPercentual de ratos: {(rato/cobaia)*100:.2f} %\nPercentual de sapos: {(sapo/cobaia)*100:.2f} %')