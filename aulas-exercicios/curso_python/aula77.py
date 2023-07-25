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
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}

d2 = copy.deepcopy(d1) #faz copia total

d2['c1'] = 1000
d2['l1'][1] = 999999
print(d1)
print(d2)