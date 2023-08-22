# Yeld from

def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN 1') 
    
def gen2(gen):
    print('COMEÇOU GEN2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN 2') 
    
def gen3():
    print('COMEÇOU GEN3')
    yield 7
    yield 8
    yield 9
    print('ACABOU GEN3') 

g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)