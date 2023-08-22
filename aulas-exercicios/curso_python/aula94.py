# Introdução as Generator functions em Python
# generator = (n for n in range(100000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
         
        if n > maximum:
            return 
        
       
    '''yield 1 # Pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais uma...')
    yield 3
    print('Vou terminar.')
    return 'ACABOU'''

gen = generator(n=5, maximum=8)
for n in gen:
    print(n)
