print('*** Convertidor de temperaturas ***')

def celcius_a_farenheit(gdoc):
    resultado = gdoc * 9/5 +32
    return resultado
def farenheit_a_celsius(gdof):
    resultado = (gdof-32) * 5/9
    return resultado

celsius = int(input('Ingresa los grados Celsius a convertir: '))
farenheit = int(input('Ingresa los grados Farenheit a convertir: '))

print(f'Resultado de Celsius a Farnheit:{celcius_a_farenheit(celsius)}')
print(f'Resultado de Farnheit a Celsius:{farenheit_a_celsius(farenheit)}')