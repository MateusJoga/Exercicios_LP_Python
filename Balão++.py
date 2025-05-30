entrada = input('')
entrada = entrada.split(' ')

raio = int(entrada[0])
helio = int(entrada[1])
pi = 3.1415

volume = (4/3) * (pi * (raio**3))

baloes = helio / volume
print(f'{int(baloes)}')