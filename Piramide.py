entrada = input('Digite um número de 1 a 26 e se serão maiusculas ou minusculas: ')
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista = entrada.split(' ')
quantponto = 0
quantletra =0
letrasF = ''
calculo = int(lista[0])

while quantponto < calculo:
    quantponto +=1
    
    for i in letras[quantletra]:
       letrasF = letrasF+str(i)
       quantletra +=1

    if lista[1] == 'maiuscula':
        print(f'{ (26 - quantponto) * '.'}{letrasF}')
    else:
        print(f'{ (26 - quantponto) * '.'}{letrasF.lower()}')