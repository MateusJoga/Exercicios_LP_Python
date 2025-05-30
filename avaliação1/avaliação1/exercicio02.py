import pickle

def remover_duplicados(lista_carregada):
    lista_carregada = set(lista_carregada)
    return list(lista_carregada)

def numero_ocorrencias(lista_carregada):
    list_ocor = {}
    for palavra in lista_carregada:
        contador = 0
        for valor in lista_carregada:
            if valor == palavra:
                contador += 1
        if palavra not in list_ocor:
            list_ocor[palavra] = contador
    return list_ocor


with open("exercicio02.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

print(lista_carregada)
lista_sem_duplicacao = remover_duplicados(lista_carregada)
print(lista_sem_duplicacao)
dicionario_ocorrencia = numero_ocorrencias(lista_carregada)
print(dicionario_ocorrencia)