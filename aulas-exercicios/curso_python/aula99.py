# Modelos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

'''import sys

#sys.exit()
platform = 'A MINHA'
print(sys.platform)
print(platform)'''

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# alias 1 - import nome_modulo as apelido
'''import sys as s

sys = 'aluma coisa'
print(s.platform)'''
# alias 2 - from nome_modulo import objeto as apelido
'''
from sys import exit as ex
from sys import platform as pl
'''
# Vantagens: você pode reservar nome para seu código
# Desvantagens: pode ficar fora do padrão da linguagem


# má prática - from nome_modulo import*
# Vantagens: importa tudo de módulo
# Desvantagens: importa tudo de um módulo
from sys import *

print(platform)
exit()
