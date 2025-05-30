entrada = input('Digite um texto: ').split(' ')
dicionario = {}
pos = 0

for palavra in entrada:
    quantidade = entrada.count(str(palavra))
    if palavra not in dicionario.keys():
        dicionario[palavra] = quantidade
    else:
        continue 

print(dicionario)

for chave in dicionario.keys():
    pos += 1
    print(f'A {pos}° chave é: |{chave}| - Contém: {dicionario.get(chave)}')