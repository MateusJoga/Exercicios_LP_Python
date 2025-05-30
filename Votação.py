contador = 0
candidato = [0, 0, 0, 0, 0, 0]

while contador < 20:
    voto = int(input('Digite o seu voto: '))
    candidato[voto-1] += 1
    contador +=1

for i in range(0,6):
    
    if i == 4:
        print(f'Quantidade total de votos NULOS: {candidato[4]}')
    elif i == 5:
        print(f'Quantidade total de votos BRANCOS: {candidato[5]}')
    else:
        print(f'Quantidade total de votos do {i+1}°Candidato: {candidato[i]}')

print(f'Quantidade total de votos NULOS: {(candidato[4]/contador) * 100}%')
print(f'Quantidade total de votos BRANCO: {(candidato[5]/contador) * 100}%')