'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibidade para o usuário digitar apenas uma letra.
-Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta
.... - Se a letra digitada estiver na palavra secreta; exiba a letra;
.... - Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
'''

'''palavra_secreta = 'computador'
letras_corretas = []
tentativas = 0

print("Bem-vindo ao jogo da adivinhação de palavras!")
print("A palavra tem", len(palavra_secreta), "letras.")

while True:
    acertos = 0
    for letra in palavra_secreta:
        if letra in letras_corretas:
            print(letra, end=' ')
            acertos += 1
        else:
            print('*', end=' ')
    
    if acertos == len(palavra_secreta):
        print("\nParabéns! Você acertou a palavra secreta:", palavra_secreta)
        print("Número de tentativas:", tentativas)
        break

    print("\nTentativas feitas:", tentativas)
    usuario = input('Digite uma letra: ').lower()

    if len(usuario) != 1 or not usuario.isalpha():
        print('Digite apenas uma letra válida.')
        continue

    if usuario in letras_corretas:
        print('Você já tentou essa letra antes.')
        continue

    letras_corretas.append(usuario)

    if usuario not in palavra_secreta:
        print('A letra não está na palavra secreta. Tente novamente!!')

    tentativas += 1 '''
    
import os
    
palavra_secreta = 'perfume' 
letras_acertadas = ''  
tentativas = 0 
    
while True:
    letra__digitada = input('Digite uma letra: ')
    tentativas += 1 
    
    if len(letra__digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra__digitada in palavra_secreta:
        letras_acertadas += letra__digitada
        
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!!')
        print('A palavra era', palavra_formada)
        print('Tentativas:', tentativas)
        letras_acertadas = ''  
        tentativas = 0 

    
    
        



        
    
    
    
    
