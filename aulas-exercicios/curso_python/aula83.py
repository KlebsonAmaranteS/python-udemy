'''
Função lambda em Python
A função lambda é uma função como qualquer outra em python. Porém, são funções anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
'''


'''
'''
lista= [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Klebson', 'sobrenome': 'Amarante'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline','sobrenome': 'Souza'},
]

'''def ordena(item):
    #print(item)
    return item['sobrenome']
'''
'''lista.sort(key=lambda item: item['nome'])'''
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
#sorted(lista)
#print(lista)

exibir(l1)
exibir(l2)

'''for item in lista:
    print(item)'''