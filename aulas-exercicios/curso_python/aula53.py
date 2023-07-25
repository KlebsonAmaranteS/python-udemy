import os

inserir_produtos = []

while True:
    user = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ').lower()
    os.system('cls')
    
    if user == 'i':
        produto_inserido = input('Digite o nome do produto: ')
        inserir_produtos.append(produto_inserido)
        continue
    if user == 'a':
        if inserir_produtos == []:
            print('Não há produtos para apagar.')
        else:
            try:
                produto_apagado = int(input('Digite o índice do produto a ser apagado: '))
                if 0 <= produto_apagado < len(inserir_produtos):
                    inserir_produtos.pop(produto_apagado)
                else:
                    print('Índice inválido. Nenhum produto foi apagado.')
            except ValueError:
                print('Índice inválido. Certifique-se de digitar um número inteiro.')
        continue
    if user == 'l':
        if inserir_produtos == []:
            print('Não há produtos para listar.')
        else:
            tamanho_lista = len(inserir_produtos)
            for i in range(tamanho_lista):
                print(f'Produto {i}: {inserir_produtos[i]}')
