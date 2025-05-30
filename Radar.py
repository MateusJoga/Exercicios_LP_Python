velocidade = int(input('Digite a velocidade'))

if velocidade * 0.07 <= 7:
    print(f'{velocidade + 7}')
else:
    radar = velocidade * 1.07
    radarS = str(radar)
    div = radarS.split('.')
    if int(div[1]) < 5:
        print(f'{int(radar)}')
    else:
        print(f'{int(radar)+1}')

