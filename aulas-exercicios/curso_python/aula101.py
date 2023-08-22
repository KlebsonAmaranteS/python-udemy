import importlib

import aula101_m

print(aula101_m.variavel)

for i in range(10):
    importlib.reload(aula101_m)
    print(i)
    
    
print('Fim')