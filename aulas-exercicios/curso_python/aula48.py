'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: 
.... append: adiciona um item ao final
.... insert: aidiciona um item ao indice escolhido
.... pop: Remove do final ou do indice escolhido
.... del: apaga um indice
.... clear: limpa a lista
.... extend: estende a lista 
.... +: concatena listas
Create Read Update ... Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

#string = 'ABCDE'
#print(bool(lista)) false
#print(lista, type(lista))
#.........0...1.....2....3....4
#lista = [123, True, 'Luiz Otávio', 1.#2, []]
#lista[2] = 'Maria'
#print(lista)
#print(lista[2], type(lista[2]))

#lista = [10,20,30,40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
#lista.append(50)
#lista.pop()
#lista.append(60)
#lista.append(70)
#lista.pop()
#print(lista)
#ultimo_valor = lista.pop(3)
#print(lista, 'Removido,', ultimo_valor)

#........0...1..2..3
'''lista = [10,20,30,40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(100, 5)
print(lista)'''

'''lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)'''

'''
Cuidados com dados mutáveis
= - copiando valor (imutáveis)
= - aponta para o mesmo valor na memoria
'''

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)



