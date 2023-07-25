'''
args - Argumentos não nomeados
* _ * args (empacotamento e desempacotamento)
'''

#Lembre-te de desempacotamento
x,y, *resto = 1,2,3,4
print(x,y,resto)

#def soma(x,y):
    #return x+y

def soma(*args):#args empacota as informações
    total = 0
    for numero in args:
        print('Total', total)
        total += numero
        print('Total', total, numero)
    
soma(1,2,3,4,5,6)