# Convertir un número decimal a binario (0 y 1)
def decimal_binario(numero):
    if numero == 0:
        return '0'
    residuos = []
    
    while numero > 0:
        residuo = numero % 2
        residuos.append(str(residuo))
        numero = numero // 2
        
    residuos.reverse()
    return ''.join(residuos)
    
numero = int(input('Ingresa un número para convertirlo a binario: '))
print(f'El número {numero} en binario es: {decimal_binario(numero)}')