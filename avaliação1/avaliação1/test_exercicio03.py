import pickle
from exercicio03 import buscar_pessoa_por_cidade, buscar_pessoa_por_numero, buscar_pessoa_por_numero_e_cidade

with open("exercicio03.bin", "rb") as arquivo:
    lista_carregada = pickle.load(arquivo)

### Testes para a função buscar_pessoa_por_cidade ###
def test_buscar_pessoa_por_cidade_geral():
    resultado = buscar_pessoa_por_cidade(lista_carregada, 'Rio Claro')
    assert len(resultado) == 8
    for pessoa in resultado:
        assert pessoa[1].lower() == 'rio claro'

def test_buscar_pessoa_por_cidade_sem_resultados():
    resultado = buscar_pessoa_por_cidade(lista_carregada, 'São Paulo')
    assert len(resultado) == 0

def test_buscar_pessoa_por_cidade_case_insensitive():
    resultado = buscar_pessoa_por_cidade(lista_carregada, 'riO cLArO')
    assert len(resultado) == 8

def test_buscar_pessoa_por_cidade_com_resultados():
    resultado = buscar_pessoa_por_cidade(lista_carregada, 'Piracicaba')
    assert len(resultado) == 7
    for pessoa in resultado:
        assert pessoa[1].lower() == 'piracicaba'

def test_buscar_pessoa_por_cidade_com_uma_pessoa():
    resultado = buscar_pessoa_por_cidade(lista_carregada, 'Santa Gertrudes')
    assert len(resultado) == 7

### Testes para a função buscar_pessoa_por_numero ###
def test_buscar_pessoa_por_numero_geral():
    resultado = buscar_pessoa_por_numero(lista_carregada, 50)
    assert len(resultado) == 11
    for pessoa in resultado:
        assert pessoa[2] <= 50

def test_buscar_pessoa_por_numero_sem_resultados():
    resultado = buscar_pessoa_por_numero(lista_carregada, 10)
    assert len(resultado) == 0

def test_buscar_pessoa_por_numero_com_resultados():
    resultado = buscar_pessoa_por_numero(lista_carregada, 40)
    assert len(resultado) == 7
    for pessoa in resultado:
        assert pessoa[2] <= 40

def test_buscar_pessoa_por_numero_com_valor_mais_alto():
    resultado = buscar_pessoa_por_numero(lista_carregada, 100)
    assert len(resultado) == 30

def test_buscar_pessoa_por_numero_com_valor_mais_baixo():
    resultado = buscar_pessoa_por_numero(lista_carregada, 0)
    assert len(resultado) == 0 


### Testes para a função buscar_pessoa_por_numero_e_cidade ###
def test_buscar_pessoa_por_numero_e_cidade_geral():
    resultado = buscar_pessoa_por_numero_e_cidade(lista_carregada, 'Rio Claro', 50)
    assert len(resultado) == 4  # Espera-se 4 pessoas de Rio Claro com número <= 50
    for pessoa in resultado:
        assert pessoa[1].lower() == 'rio claro'
        assert pessoa[2] <= 50

def test_buscar_pessoa_por_numero_e_cidade_sem_resultados():
    resultado = buscar_pessoa_por_numero_e_cidade(lista_carregada, 'São Paulo', 50)
    assert len(resultado) == 0 

def test_buscar_pessoa_por_numero_e_cidade_com_resultados():
    resultado = buscar_pessoa_por_numero_e_cidade(lista_carregada, 'Araras', 40)
    assert len(resultado) == 1
    for pessoa in resultado:
        assert pessoa[1].lower() == 'araras'
        assert pessoa[2] <= 40

def test_buscar_pessoa_por_numero_e_cidade_case_sensitive():
    resultado = buscar_pessoa_por_numero_e_cidade(lista_carregada, 'riO cLArO', 40)
    assert len(resultado) == 2  
    for pessoa in resultado:
        assert pessoa[1].lower() == 'rio claro'
        assert pessoa[2] <= 40

def test_buscar_pessoa_por_numero_e_cidade_sem_resultados_por_numero():
    resultado = buscar_pessoa_por_numero_e_cidade(lista_carregada, 'Santa Gertrudes', 10)
    assert len(resultado) == 0  

test_buscar_pessoa_por_cidade_geral()
test_buscar_pessoa_por_cidade_sem_resultados()
test_buscar_pessoa_por_cidade_case_insensitive()
test_buscar_pessoa_por_cidade_com_resultados()
test_buscar_pessoa_por_cidade_com_uma_pessoa()
test_buscar_pessoa_por_numero_geral()
test_buscar_pessoa_por_numero_sem_resultados()
test_buscar_pessoa_por_numero_com_resultados()
test_buscar_pessoa_por_numero_com_valor_mais_alto()
test_buscar_pessoa_por_numero_com_valor_mais_baixo()
test_buscar_pessoa_por_numero_e_cidade_geral()
test_buscar_pessoa_por_numero_e_cidade_sem_resultados()
test_buscar_pessoa_por_numero_e_cidade_com_resultados()
test_buscar_pessoa_por_numero_e_cidade_sem_resultados_por_numero()
test_buscar_pessoa_por_numero_e_cidade_case_sensitive()