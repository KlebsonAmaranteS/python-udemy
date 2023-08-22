# Try, except, else e finally

try:
    print('ABRIR O ARQUIVO')
    # 8 / 0
except ZeroDivisionError:
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
