def fraccionario_binario(numero, precision=10):
    entero = int(numero)             # Parte entera (como entero)
    decimal = numero - entero        # Parte decimal (fraccionaria)
    
    # Convertir parte entera con bin()
    bin_entero = bin(entero)[2:]
    
    # Convertir parte decimal con multiplicaciones sucesivas
    bin_decimal = ''
    contador = 0
    while decimal > 0 and contador < precision:
        decimal *= 2
        bit = int(decimal)
        bin_decimal += str(bit)
        decimal -= bit
        contador += 1
    
    # Devolver resultado combinando partes
    if bin_decimal:
        return f'{bin_entero}.{bin_decimal}'
    else:
        return bin_entero

# Ejemplo
num = float(input("Ingresa un número decimal: "))
print(f"El número {num} en binario es: {fraccionario_binario(num)}")