joao = {'arroz','feijão','macarrão','leite'}
maria = {'leite','café','açúcar','arroz'}

comum = joao & maria
print(f'Os itens em comum de João e Maria são: {comum}')

dif = maria - joao
print(f'Maria comprou {dif} e João não.')

uni = joao | maria
print(f'Todos os produtos são: {uni}')