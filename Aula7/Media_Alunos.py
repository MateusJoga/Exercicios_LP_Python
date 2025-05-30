boletim = {
    "Ana": (8.0 , 7.5),
    "Carlos": (5.0, 6.0),
    'Beatriz': (9.0, 8.5),
    'Daniel': (6.0, 6.5)
    }
mediadict = {}

def media():

    print('Médias dos alunos:')
    for nome, nota in boletim.items():
        media = (nota[0] + nota[1])/2
        mediadict[nome] = media
        print(f'{nome}: {(media)}')

    print('Aprovados:')
    for nome, nota in mediadict.items():
        if nota >= 7:
            print(f'{nome}')
    
    print('Reprovados:')
    for nome, nota in mediadict.items():
        if nota < 7:
            print(f'{nome}')

media()