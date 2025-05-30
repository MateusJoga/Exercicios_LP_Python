import pickle

def buscar_pessoa_por_cidade(lista_carregada, cidade):
    cidade = cidade.lower()
    print(cidade)
    list_cid = []
    for nome, cidad, num in lista_carregada:
        if cidad.lower() == cidade:
            list_cid.append((nome, cidad, num))
        else:
            continue
    return list_cid



def buscar_pessoa_por_numero(lista_carregada, numero):
    list_num = []
    for nome, cidad, num in lista_carregada:
        if num <= numero:
            list_num.append((nome, cidad, num))
        else:
            continue
    return list_num

def buscar_pessoa_por_numero_e_cidade(lista_carregada, cidade, numero):
    cidade = cidade.lower()
    list_ord = []
    for nome, cidad, num in lista_carregada:
        if num <= numero and cidad.lower() == cidade:
            list_ord.append((nome, cidad, num))
        else:
            continue
    return list_ord

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(buscar_pessoa_por_cidade(lista_carregada, 'rio claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'rio Claro'))
# print(buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro'))

print(buscar_pessoa_por_numero(lista_carregada, 20))
# print(buscar_pessoa_por_numero(lista_carregada, 29.8))

print(buscar_pessoa_por_numero_e_cidade(lista_carregada, 'rio claro', 40))
