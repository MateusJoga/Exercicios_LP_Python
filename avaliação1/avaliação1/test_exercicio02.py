from exercicio02 import remover_duplicados, numero_ocorrencias

def test_remover_duplicados_com_repetidos():
    lista = ["Ana", "Bruno", "Ana", "Carla", "Bruno"]
    resultado = remover_duplicados(lista)
    esperado = set(["Ana", "Bruno", "Carla"])
    assert set(resultado) == esperado
    assert len(resultado) == 3

def test_remover_duplicados_sem_repetidos():
    lista = ["Ana", "Bruno", "Carla"]
    resultado = remover_duplicados(lista)
    assert type(lista) == type([])
    assert set(resultado) == set(lista)
    assert len(resultado) == 3

def test_remover_duplicados_lista_vazia():
    lista = []
    resultado = remover_duplicados(lista)
    assert resultado == []

def test_remover_duplicados_todos_iguais():
    lista = ["Ana"] * 10
    resultado = remover_duplicados(lista)
    assert resultado == ["Ana"] or set(resultado) == {"Ana"}
    assert len(resultado) == 1

def test_remover_duplicados_50_itens_com_35_unicos():
    lista = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fábio", "Gabriela", "Henrique",
             "Isabela", "João", "Karla", "Lucas", "Mariana", "Nicolas", "Olívia", "Pedro",
             "Quezia", "Rafael", "Sabrina", "Tiago", "Ursula", "Vinícius", "Wesley", "Ximena",
             "Yasmin", "Zeca", "Amanda", "Bianca", "Caio", "Douglas", "Elaine", "Fernando",
             "Gustavo", "Heloísa", "Ícaro",
             "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fábio", "Gabriela", "Henrique",
             "Isabela", "João", "Karla", "Lucas", "Mariana", "Nicolas", "Olívia"]
    
    resultado = remover_duplicados(lista)
    assert len(resultado) == 35
    assert set(resultado).issubset(set(lista))


def test_ocorrencias_lista_simples():
    lista = ["Ana", "Bruno", "Carlos", "Ana", "Carlos", "Carlos"]
    resultado = numero_ocorrencias(lista)
    assert resultado == {"Ana": 2, "Bruno": 1, "Carlos": 3}

def test_ocorrencias_lista_sem_repeticao():
    lista = ["Ana", "Bruno", "Carlos"]
    resultado = numero_ocorrencias(lista)
    assert resultado == {"Ana": 1, "Bruno": 1, "Carlos": 1}

def test_ocorrencias_lista_vazia():
    lista = []
    resultado = numero_ocorrencias(lista)
    assert resultado == {}

def test_ocorrencias_lista_uma_pessoa_repetida():
    lista = ["Ana", "Ana", "Ana"]
    resultado = numero_ocorrencias(lista)
    assert resultado == {"Ana": 3}

def test_ocorrencias_lista_com_espacos_ou_formatos_diferentes():
    lista = ["Ana", "ana", " ANA", "Ana"]
    resultado = numero_ocorrencias(lista)
    assert resultado == {"Ana": 2, "ana": 1, " ANA": 1}

test_remover_duplicados_com_repetidos()
test_remover_duplicados_sem_repetidos()
test_remover_duplicados_lista_vazia()
test_remover_duplicados_todos_iguais()
test_remover_duplicados_todos_iguais()
test_remover_duplicados_50_itens_com_35_unicos()
test_ocorrencias_lista_simples()
test_ocorrencias_lista_sem_repeticao()
test_ocorrencias_lista_vazia()
test_ocorrencias_lista_uma_pessoa_repetida()
test_ocorrencias_lista_com_espacos_ou_formatos_diferentes()