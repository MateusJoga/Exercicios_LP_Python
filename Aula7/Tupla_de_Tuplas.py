carrinho = (
    ("Arroz", 24.90),
    ("Feijão", 8.50),
    ("Leite", 4.80)
)

for prod,valor in carrinho:
    print(f'Produto: {prod} | Preço: R$ {valor:.2f}')