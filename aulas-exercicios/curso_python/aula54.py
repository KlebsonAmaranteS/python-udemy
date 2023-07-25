'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://pt.wikipedia.org/wiki/Dupla_precis%C3%A3o_no_formato_de_ponto_flutuante
https://docs.python.org/3/tutorial/floatingpoint.html
'''
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))