'''
Exercicio:
Sistema de perguntas e respostas
'''


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i}) {opcao}")
    resposta_usuario = int(input('Escolha uma opção (digite o número da opção): '))
    
    if resposta_usuario == pergunta['Opções'].index(pergunta['Resposta']):
        print('Acertou 👍')
        acertos += 1
    else:
        print('Errou 👎')
        erros += 1

    print()

print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}") 