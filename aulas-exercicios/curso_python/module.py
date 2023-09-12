import json, os

pessoas = [
    {
        "nome": 'Maria',
        'sobrenome': 'Vieira',
        'idade': 25,
        'ativo': False,
        'notas': ['A', 'A+'],
        'telefones': {
            'residencial': "3361-2699",
            'celular': "99876-5432"
        }
    },
    {
        "nome": "Joana",
        "sobrenome": "Moreira",
        "idade": 32,
        "ativo": True,
        "notas": ['B', 'A'],
        'telefones': {
            'residencial': "3361-2699",
            'celular': "99876-5432"
        }
    },
]

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE, "r") as file:
    pessoas = json.load(file)
    print(json.dumps(pessoas))
    
    # for pessoa in pessoas:
    #     print(pessoa['nome'])
    # print(pessoas)
#     json.dump(pessoas, file, indent=2)
    
# print(json.dumps(pessoas))