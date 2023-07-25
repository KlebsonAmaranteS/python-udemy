'''
Exercicios 
- Crie funções que duplicam, triplicam e quadriplicam o numero como parâmetro.
'''

'''def duplicar(numero):
    return numero * 2
def triplica(numero):
    return numero * 3
def quadruplica(numero):
    return numero * 4

print(duplicar(2))
print(triplica(2))
print(quadruplica(2))'''

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplicar = criar_multiplicador(2) 
triplicar = criar_multiplicador(3) 
quadruplicar = criar_multiplicador(4) 

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
