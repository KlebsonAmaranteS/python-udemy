'''
Dicionarios em Python (tipo dict)
Dicionarios são estruturas de dados do tipo par de 'chave' e 'valor'
Chaves podem ser consideradas 'indices' que vimos na lista e podem ser de tipos imútaveis como: str, int, float, bool, tuple, etc...
O valor pode ser qualquer tipo, incluindo outro dicionario.
Usamos as chaves - {} - ou a classe dict para criar dicionarios
Imútaveis: str, int, float, bool, tuple
Mútavel: dict, list

pessoa = {
    'nome': 'Luiz Otávio,
    'sobrenome': 'Miranda',
    'idade': 25,
    'peso': 65.4,
    'altura': 1.75,
    'enderecos':[
        {'rua': 'Rua 1', 'numero': 100},
        {'rua': 'Rua 2', 'numero': 200}
    ]
}
print(pessoa, type(pessoa))
'''
pessoa = {
    'nome': 'Klebson Amarante',
    'sobrenome': 'da Silva',
    'idade': 21,
    'peso': 75.4,
    'altura': 1.80,
    'enderecos':[
        {'rua': 'Rua 1', 'numero': 100},
        {'rua': 'Rua 2', 'numero': 200},
    ]
}
#pessoa = dict(nome='Klebson', sobrenome='Amarante')
#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])