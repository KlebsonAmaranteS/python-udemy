'''
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
For + Range
range -> range(start, stop, step)
'''
#numeros = range(0, -10, -2)

#for numero in numeros:
    #print(numero)
    


texto = 'Klebson' # iterável
#iterador = iter(texto) # iterator

#while True:
    #try:
     #letra = next(iterador)
     #print(letra)
    #except StopIteration:
        #break
        
for letra in texto:
    print(letra)
    