from exercicio01 import menores_idade 

def test_menores_idade_alguns_menores():
    lista = [("Ana", 17), ("Bruno", 18), ("Carlos", 16)]
    esperado = [("Ana", 17), ("Carlos", 16)]
    assert menores_idade(lista) == esperado

def test_menores_idade_nenhum_menor():
    lista = [("Diana", 18), ("Eduardo", 22), ("Fernanda", 34)]
    esperado = []
    assert menores_idade(lista) == esperado

def test_menores_idade_todos_menores():
    lista = [("Gabriel", 14), ("Helena", 16), ("Igor", 17)]
    esperado = [("Gabriel", 14), ("Helena", 16), ("Igor", 17)]
    assert menores_idade(lista) == esperado

def test_menores_idade_lista_vazia():
    lista = []
    esperado = []
    assert menores_idade(lista) == esperado

def test_menores_idade_limite_18():
    lista = [("Julia", 18), ("Kaio", 17)]
    esperado = [("Kaio", 17)]
    assert menores_idade(lista) == esperado