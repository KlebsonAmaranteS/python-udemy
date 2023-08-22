# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos sys.path
import aula100_m
from aula100_m import soma, variavel_modulo

# O módulo __main__ é executado quando o arquivo é chamado diretamente

print(variavel_modulo)
#print('Este módulo se chama', __name__)
print(aula100_m.variavel_modulo)
print(soma(2,3))
print(aula100_m.soma(2,3))
