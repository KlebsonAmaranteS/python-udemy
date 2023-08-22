#Exercicios 
#Aumente os preços dos produtos a seguir em 10%
#Gere novos_produtos por deep copy
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

# Função para aumentar os preços em 10%
def aumentar_precos(produtos):
    novos_produtos = copy.deepcopy(produtos)
    for produto in novos_produtos:
        produto['preco'] *= 1.10  # Aumento de 10%
    return novos_produtos

novos_produtos = aumentar_precos(produtos)

# Imprimindo os novos produtos
for produto in novos_produtos:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']:.2f}")

#Ordene os produtos por nome descrecente (do maior para o menor) gere_produtos_ordenados_por_nome por deep copy (cópia profunda)

print('\n')

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)

print(produtos_ordenados_por_nome, sep='\n')

print('\n')
#Ordene os produtos por preço crescente (do menor para o maior) gere produtos_ordenados_por_preco por deep copy(cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'])

print(produtos_ordenados_por_preco, sep='\n')