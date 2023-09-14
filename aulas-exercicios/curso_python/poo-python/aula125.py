# Métodos em instâncias de classes Python.
# Hard coded - É algo que foi escrito diretamente no código.
# Instancia da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
        
fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)     
 
# string = 'Luiz'
# print(string.upper())

fusca = Carro('Fusca')
# print(fusca.nome)
# fusca.acelerar()

celta = Carro('Celta')
Carro.acelerar(celta)
# print(celta.nome)
celta.acelerar()
