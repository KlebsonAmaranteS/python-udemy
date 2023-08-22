# Exercicio - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem
# Ex: ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#MEU CODIGO
# cidades_lista = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados_lista = ['BA', 'SP', 'MG', 'RJ']

# def zipper(cidades, estados):
#     tamanho_lista = min(len(cidades), len(estados))
    
#     resultado = [(cidades[i], estados[i]) for i in range(tamanho_lista)]
    
#     return resultado

# resultado_lista = zipper(cidades_lista, estados_lista) 
# print(resultado_lista)


#CODIGO DA AULA
# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     ]
    
#CODIGO AULA MELHORADO
from itertools import zip_longest
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1,l2)))
print(list(zip_longest(l1,l2, fillvalue='SEM CIDADE')))

