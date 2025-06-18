print('*** Valor dentro del rango ***')
VALOR_MINIMO = 0
VALOR_MAXIMO = 5
valor = int(input(f'Ingresa un número entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

esta_dentro_del_rango = (valor >= VALOR_MINIMO) and (valor <= VALOR_MAXIMO)
# esta_dentro_del_rango = VALOR_MINIMO <= VALOR <= VALOR_MAXIMO
print(f'El valor de {valor} está dentro del rango? {esta_dentro_del_rango}')