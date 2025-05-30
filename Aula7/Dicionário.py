tabela = {
    "Arroz": 24.90,
    "Feijão": 8.50,
    "Leite": 4.80,
    "Açúcar": 3.90
}

print(f'Preço do Leite: R$ {tabela['Leite']:.2f}\nPreço do Feijão: R$ {tabela['Feijão']:.2f}')

tabela['Café'] = 14.20
tabela["Açúcar"] = 4.10

print(tabela)