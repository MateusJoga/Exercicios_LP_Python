lista = input('')
listaordem = lista.split(' ')
linha = int(listaordem[0])
coluna = int(listaordem[1])
bateria = int(listaordem[2])
andar = 0
batidas = 0

listaPos = input('')
listaordemPos = listaPos.split(' ')
posX = int(listaordemPos[0])
posY = int(listaordemPos[1])

mov = input('')
listaMov = list(mov)

for i in listaMov:
    if i == 'B':
        posY +=1
        if posY > coluna:
            posY -= 1
            batidas += 1
    if i == 'C':
        posY -=1
        if posY < 1:
            posY +=1
            batidas += 1
    if i == 'D':
        posX +=1
        if posX > linha:
            posX -= 1
            batidas += 1
    if i == 'E':
        posX -=1
        if posX < 1:
            posX +=1
            batidas += 1
    andar += 1
    if andar == bateria:
        break

print(f'{posY} {posX} {batidas}')