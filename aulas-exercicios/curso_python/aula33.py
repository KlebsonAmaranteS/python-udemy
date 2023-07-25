'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
'''num = input("Digite um número inteiro: ")

if num.isdigit():
    numero = int(num)
    
    if numero % 2 == 0:
        print("O número {} é par".format(num))
    else:
        print(f"O número {num} é impar.")
else:
    print("O valor digitado NÃO é um número inteiro")'''
'''

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. EX: Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
'''

'''horas = input("Que horas são? ")

try:
    
    hora = int(horas)
    bom_dia = hora >= 0 and hora <= 11
    boa_tarde = hora >= 12 and hora <= 17
    boa_noite = hora >= 18 and hora <= 23

    if bom_dia:
        print("Bom dia")
    elif boa_tarde:
        print("Boa tarde")
    elif boa_noite:
        print("Boa noite")
    else:
        print('Não conheço essa hora.')
except:
    print('Por favor, digite apenas números inteiros.')'''

'''Faça um programa que peça o primeiro nome do usuário, se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
'''

primeiro_nome = input("Digite seu primeiro nome: ")

if len(primeiro_nome) > 1:
    if len(primeiro_nome) <= 4:
        print("Seu nome é curto")
    elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
        print("Seu nome é normal")
    else:
        print('Seu nome é muito grande.')
else:
    print("Por favor, digite mais de uma letra.") 