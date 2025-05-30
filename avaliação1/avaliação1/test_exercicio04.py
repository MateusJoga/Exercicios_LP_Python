from exercicio04 import media_nota, situacao_falta, acima_de_nove, uma_nota_abaixo_de_seis

# Lista base para os testes
alunos = [
    ("Ana", 9.0, 9.5, 9.0, 2),
    ("Bruno", 5.0, 6.0, 7.0, 7),
    ("Carlos", 10.0, 10.0, 10.0, 1),
    ("Daniela", 5.5, 6.5, 4.0, 3),
    ("Eduardo", 6.0, 6.0, 6.0, 6)
]

# Testes para media_nota
def test_media_nota_ana():
    resultado = media_nota(alunos)
    assert ("Ana", 9.17) in resultado

def test_media_nota_bruno():
    resultado = media_nota(alunos)
    assert ("Bruno", 6.0) in resultado

def test_media_nota_carlos():
    resultado = media_nota(alunos)
    assert ("Carlos", 10.0) in resultado

def test_media_nota_daniela():
    resultado = media_nota(alunos)
    assert ("Daniela", 5.33) in resultado

def test_media_nota_edurado():
    resultado = media_nota(alunos)
    assert ("Eduardo", 6.0) in resultado

# Testes para situacao_falta
def test_situacao_falta_aprovado():
    resultado = situacao_falta(alunos)
    assert ("Ana", "Aprovado") in resultado

def test_situacao_falta_reprovado():
    resultado = situacao_falta(alunos)
    assert ("Bruno", "Reprovado") in resultado

def test_situacao_falta_reprovado_limite():
    resultado = situacao_falta(alunos)
    assert ("Eduardo", "Reprovado") in resultado

def test_situacao_falta_aprovado_limite():
    resultado = situacao_falta(alunos)
    assert ("Carlos", "Aprovado") in resultado

def test_situacao_falta_aprovado_geral():
    resultado = situacao_falta(alunos)
    assert len([r for r in resultado if r[1] == "Aprovado"]) == 3

# Testes para acima_de_nove
def test_acima_de_nove_carlos():
    resultado = acima_de_nove(alunos)
    assert "Carlos" in resultado

def test_acima_de_nove_ana():
    resultado = acima_de_nove(alunos)
    assert "Ana" in resultado

def test_acima_de_nove_nenhum_outro():
    resultado = acima_de_nove(alunos)
    assert "Bruno" not in resultado

def test_acima_de_nove_quantidade():
    resultado = acima_de_nove(alunos)
    assert len(resultado) == 2

def test_acima_de_nove_tipo():
    resultado = acima_de_nove(alunos)
    assert all(isinstance(nome, str) for nome in resultado)

# Testes para uma_nota_abaixo_de_seis
def test_uma_nota_bruno():
    resultado = uma_nota_abaixo_de_seis(alunos)
    assert ("Bruno", 5.0, 6.0, 7.0) in resultado

def test_uma_nota_daniela():
    resultado = uma_nota_abaixo_de_seis(alunos)
    assert ("Daniela", 5.5, 6.5, 4.0) in resultado

def test_uma_nota_carlos():
    resultado = uma_nota_abaixo_de_seis(alunos)
    assert not any("Carlos" in r for r in resultado)

def test_uma_nota_ana():
    resultado = uma_nota_abaixo_de_seis(alunos)
    assert ("Ana", 9.0, 9.5, 9.0) not in resultado

def test_uma_nota_tamanho():
    resultado = uma_nota_abaixo_de_seis(alunos)
    assert len(resultado) == 2

test_media_nota_ana()
test_media_nota_bruno()
test_media_nota_carlos()
test_media_nota_edurado()
test_situacao_falta_aprovado()
test_situacao_falta_reprovado()
test_situacao_falta_reprovado_limite()
test_situacao_falta_aprovado_limite()
test_situacao_falta_aprovado_geral()
test_acima_de_nove_carlos()
test_acima_de_nove_ana()
test_acima_de_nove_nenhum_outro()
test_acima_de_nove_quantidade()
test_acima_de_nove_tipo()

test_uma_nota_bruno()
test_uma_nota_daniela()
test_uma_nota_carlos()
test_uma_nota_ana()
test_uma_nota_tamanho()