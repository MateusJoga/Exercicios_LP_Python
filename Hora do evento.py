dia_inicio = int(input('Digite o dia de inicio: '))
hora_inicio = input('Digite o horario em hh:mm:ss - ')
dia_final = int(input('Digite o dia de término: '))
hora_final = input('Digite o horario em hh:mm:ss -  ')
horarioI = hora_inicio.split(':')
horarioF = hora_final.split(':')
contador = False



if int(horarioI[2]) > int(horarioF[2]):
    segundo = 60 - int(horarioI[2]) + int(horarioF[2])
    contador = True
else:
    segundo = int(horarioF[2]) - int(horarioI[2])

if contador == True:
    if int(horarioI[1]) > int(horarioF[1]):
        minuto = 60 - int(horarioI[1]) + int(horarioF[1]) -1
    else:
        minuto = int(horarioF[1]) - int(horarioI[1]) -1
        contador = False
else:
    minuto = int(horarioF[1]) - int(horarioI[1])
    contador = False

if contador == True:
    if int(horarioI[0]) > int(horarioF[0]):
        hora = 24 - int(horarioI[0]) + int(horarioF[0]) - 1
    else:
        hora = int(horarioF[0]) - int(horarioI[0]) - 1
        contador == False
else:
    hora = int(horarioF[0]) - int(horarioI[0])
    contador == False

if contador == True:
    if dia_inicio > dia_final:
        dia = 30 - dia_final + dia_inicio - 1
    else:
        dia = dia_final - dia_inicio - 1
else:
    dia = dia_final - dia_inicio


'''
if dia_inicio > dia_final:
    dia = dia_final - dia_inicio + 30
else:
    dia = dia_final - dia_inicio
if int(horarioI[0]) > int(horarioF[0]):
    hora = int(horarioI[0]) - int(horarioF[0]) + 24
else:
    hora = int(horarioI[0]) - int(horarioF[0])
if int(horarioI[1]) > int(horarioF[1]):
    minuto = int(horarioI[1]) - int(horarioF[1]) + 60
else:
    minuto = int(horarioI[1]) - int(horarioF[1])
if int(horarioI[2]) > int(horarioF[2]):
    segundo = int(horarioI[2]) - int(horarioF[2]) + 60
else:
    segundo = int(horarioI[2]) - int(horarioF[2])
'''
    
print(f'{dia} dia(s)\n{hora} hora(s)\n{minuto} minuto(s)\n{segundo} segundo(s)')
