# Mapeamento de dados em list comprehension

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []

'''for numero in range(10):
    lista.append(numero)'''
#print(lista)

'''lista = [numero * 2 for numero in range(10)]
print(list(range(10)))
print(lista)'''

produtos = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 35},
    {'nome': 'p3', 'preço': 48},
]



#print(*novos_produtos, sep='\n')
#p(novos_produtos)

#lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preço' : produto['preço'] * 1.05} 
    if produto['preço'] > 20 else {**produto}
    for produto in produtos 
    if produto['preço'] >= 20 and produto['preço'] * 1.05
]
p(novos_produtos)