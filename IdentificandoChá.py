varT = int(input(''))
RespC = input('')
RespC = RespC.split(' ')
acertos = 0

for i in RespC:
    if i == str(varT):
        acertos +=1
    else:
        continue

print(f'{acertos}')