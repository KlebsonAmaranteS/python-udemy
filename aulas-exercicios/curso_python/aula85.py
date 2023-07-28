# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
#print(a,b)

'''
(a1,a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)'''

pessoa = {
    'nome': 'Klebson',
    'sobrenome': 'Amarante',
    
}
 
dados_pessoa = {
    'idade': 25,
    'peso': 65.4,
    'altura': 1.75
}  

pessoas_completa = {**pessoa, **dados_pessoa} 

print(pessoas_completa)
# args e kwargs
# args (já visto)
# kwargs - keyword argument (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args)
    for chave, valor in kwargs.items():
        print(chave, valor)
    
'''mostro_argumentos_nomeados(1,2, nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)'''

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)