import pickle


def media_nota(lista_carregada):
    lista_media = []
    for nome,n1,n2,n3,falta in lista_carregada:
        media = (n1+n2+n3)/3
        media = f'{media:.2f}'
        lista_media.append((nome, float(media)))
    return lista_media

def situacao_falta(lista_carregada):
    lista_falta = []
    for nome,n1,n2,n3,falta in lista_carregada:
        if falta >= 6:
            lista_falta.append((nome, 'Reprovado'))
        else:
            lista_falta.append((nome, 'Aprovado'))
    return lista_falta


def acima_de_nove(lista_carregada):
    lista_acinove = []
    for nome,n1,n2,n3,falta in lista_carregada:
        if n1+n2+n3 >= 27:
            lista_acinove.append(nome)
        else:
            continue
    return lista_acinove

def uma_nota_abaixo_de_seis(lista_carregada):
    lista_abxseis = []
    for nome,n1,n2,n3,falta in lista_carregada:
        if n1 < 6 or n2 < 6 or n3 <6:
            lista_abxseis.append((nome, n1, n2, n3))
        else:
            continue
    return lista_abxseis


with open("exercicio04.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
print(media_nota(lista_carregada))
print(situacao_falta(lista_carregada))
print(acima_de_nove(lista_carregada))
print(uma_nota_abaixo_de_seis(lista_carregada))
