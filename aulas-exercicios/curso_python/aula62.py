'''
Introdução ás funções (def) em python
Funções são trechos de código usados
para replicar determinada ação ao longo do seu código. Elas podem receber valores para parâmetros (argumentos) e retornar um valor especifico. Por padrão, funções python retornam None(nada).
'''
'''def Print(a,b,c):
        print('Varias1')
        print('Varias2')
        print('Varias3')
        print('Varias4')'''
        
'''def imprimir(a,b,c):
        print(a,b,c)

imprimir(1,2,3)
imprimir(4,5,6)'''

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')
    
saudacao('Pedro')
saudacao('Anny')
saudacao()
