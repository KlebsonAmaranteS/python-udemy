# Exercicios com funções
# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variavel

'''def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

numeros = 1,2,3, 
print(multiplicar(*numeros))'''


# Crie uma função que fala se um número é par ou impar.
# Retorne se o número é par ou impar 

def impar_par(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é impar'
    
numero = int(input('Digite um número: '))
print(impar_par(numero))