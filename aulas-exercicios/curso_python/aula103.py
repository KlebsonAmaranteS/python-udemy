'''from sys import path
import aula102_package.modulo
from aula102_package.modulo import soma_do_modulo
from aula102_package import modulo
from aula102_package.modulo import*

#print(*path, sep='\n')
print(soma_do_modulo(1,2))
print(aula102_package.modulo.soma_do_modulo(1,2))
print(modulo.soma_do_modulo(1,2))
print(variavel)
print(nova_variavel)'''

'''from aula102_package.modulo import soma_do_modulo, fala_oi

print(__name__)
fala_oi()'''


from aula102_package import soma_do_modulo, qualquer_coisa

print(soma_do_modulo(2,3))
qualquer_coisa()