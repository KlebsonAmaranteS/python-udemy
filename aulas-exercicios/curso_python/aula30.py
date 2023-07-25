'''
CONSTANTE = "variavéis" que não vão mudar
Muitas condições do mesmo if (ruim)
.... <- Contagem de complexidade (ruim)
'''

velocidade = 61 #velocidade atual do carro
local_carro = 98 #local em que o carro está na estrada



RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1.')


if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('carro multado em radar 1')
    