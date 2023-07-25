'''
Argumento nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas argumentos (valor)
'''
def soma(x,y,z):
    #Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z =', x + y + z)
    
soma(1,2,3)
soma(1,y=2,z=5)