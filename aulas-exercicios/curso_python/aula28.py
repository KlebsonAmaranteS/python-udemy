'''
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade 
Se nome e idade forem digitados 
    Exiba:
    .....Seu nome é {nome}
    .....Seu nome invertido é {nome_invertido}
    .....Se nome contém ou não espaços
    .....Seu nome tem n letras
    .....A primeira letra do seu nome é {letra}
    .....A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
....exiba "Desculpe, você deixou campos vazios."
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
contem_espaco = False
nome_sem_espacos = nome.replace(" ", "")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if ' ' in nome: 
        print('Seu nome contem espaços')
    else:
        print('Seu nome NÃO contem espaços')
        
        
    print(f"Seu nome tem {len(nome_sem_espacos)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
        
else:
    print("Desculpe, você deixou campos vazios.")
            