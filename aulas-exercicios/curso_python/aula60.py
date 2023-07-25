'''
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex: 746.824.890-70 (746824890)
... 10  9  8  7  6  5  4  3  2
... 7   4  6  8  2  4  8  9  0
... 70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11
Se o resultado anterior for maior que 9:
... O resultado é 0
contrário disso:
... resultado é o valor da conta

O primeiro digito do CPF é 7.
'''

'''cpf = '746824890'  # CPF sem pontos e hífen
soma = 0

# Etapa 1: Multiplicar cada dígito por uma contagem regressiva de 10 a 2
for i, digito in enumerate(cpf[:-2], start=2):
    soma += int(digito) * (11 - i)

# Etapa 2: Multiplicar a soma por 10
resultado = soma * 10

# Etapa 3: Obter o resto da divisão por 11
resto = resultado % 11

# Etapa 4 e 5: Verificar o valor do resto e determinar o primeiro dígito verificador
if resto > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto

print(f"O primeiro dígito verificador do CPF é: {primeiro_digito}")'''

#codigo da aula:

import re
import sys


'''cpf_enviado_usuario = '746.824.890-70'.replace('.', '').replace('-','')'''
entrada = input('CPF[746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[0:9]
dez_digitos = cpf_enviado_usuario[0:10]
contador_regressivo_1 = 10
contador_regressivo_2 = 11

resultado_digito_1 = 0
resultado_digito_2 = 0 

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2 * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é um CPF válido!')
else:
    print('CPF inválido!')   

