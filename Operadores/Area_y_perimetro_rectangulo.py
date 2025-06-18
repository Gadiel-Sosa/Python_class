print('*** Área y Perímetro de un Rectangulo **+')
base = float(input('Ingresa la base del triángulo en cm: '))
altura = float(input('Ingresa la altura del triángulo en cm: '))

while True:
    print("""
    ------ Menú ------
    1.-Área del rectángulo
    2.-Perímetro del rectángulo
    3.-Salir
    """)
    opcion = int(input('Selecciona una opción: '))
    if opcion == 1:
        area = base * altura
        print(f'El área del rectángulo es: {area}')
    elif opcion == 2:
        perimetro = 2 * (base + altura)
        print(f'El perímetro del rectángulo es: {perimetro}')
    else:
        break

