import json

pessoa = {
    'nome': 'Luiz Otavio 3',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'Rua 1', 'numero': 100},
       {'rua': 'Rua 2', 'numero': 200}
    ],
    'altura': 1.8,
    'numeros_preferidos': (2,4,6,8,10),
    'dev': True,
    'nada': None,
}

with open('aula120.json', 'w', encoding='utf8') as arquivo:
     json.dump(pessoa, 
               arquivo, 
               ensure_ascii=False, 
               indent=2)

# with open('aula120.json', 'r', encoding='utf8') as arquivo:
#           pessoa = json.load(arquivo)
#         #   print(pessoa)
#         #   print(type(pessoa))
#           print(pessoa['nome'])