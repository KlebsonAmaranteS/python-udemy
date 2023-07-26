'''
Sets - Conjuntos em python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno'''

'''Criando set
set(iterável) ou {1,2,3}'''

'''s1 = set() # vazio
s1 = {'Luiz', 1,2,3} #com dados
print(s1)'''

'''Sets são eficientes para remover valores duplicados de iteráveis
- seus valores sempre serão únicos;
- não aceitam valores mútaveis;
- eles tem indexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)'''

#s1 = {1,2,3,3,3,3,1}
'''l1 = [1,2,3,3,3,3,1]
s1 = set(l1)
l2 = list(s1)'''

'''s1 = {1,2,3}
#print(s1)

for numero in s1:
    print(numero)'''

'''
Métodos úteis:
add, update, clear, discard'''

'''s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá Mundo', 1,2,3,4))
#s1.clear()
s1.discard('Olá Mundo')
s1.discard('Luiz')
print(s1)'''

'''Operadores úteis:
união | (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simetrica ^ - Itens que não estão em ambos
'''

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3, s4, s5, s6)