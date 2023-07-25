'''
Metodos úteis dos dicionarios em Python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shalow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro

'''

pessoa = {
    'nome': 'Klebson Amarante',
    'sobrenome': 'da Silva',
    # 'idade': 22
}

pessoa.setdefault('idade', 22)
print(pessoa['idade'])

#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

'''for valor in pessoa.values():
    print(valor)'''
    
'''for chave, valor in pessoa.items():
    print(chave, valor)'''