# Exercicio com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor 
# OBS: Um motor pode ser de varios carros 
# Exiba o nome do carro, motor e fabricantes na tela


#Minha versão

# class Motor:
#     def __init__(self, nome):
#         self.nome = nome
    
# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome

# class Carro:
    
#     def __init__(self, nome, motor, fabricante):
#         self.nome = nome
#         self.motor = motor
#         self.fabricante = fabricante

# motor1 = Motor("1.0")
# motor2 = Motor("1.6")

# fabricante1 = Fabricante("Fiat")
# fabricante2 = Fabricante("Ford")

# carro1 = Carro("Uno", motor1, fabricante1)
# carro2 = Carro("Gol", motor2, fabricante2)


# print(f"Carro: {carro1.nome}")
# print(f"Motor: {carro1.motor.nome}")
# print(f"Fabricante: {carro1.fabricante.nome}")


# print(f"\nCarro: {carro2.nome}")
# print(f"Motor: {carro2.motor.nome}")
# print(f"Fabricante: {carro2.fabricante.nome}")


# Versão de aula

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)