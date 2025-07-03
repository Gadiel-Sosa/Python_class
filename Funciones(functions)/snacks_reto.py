print('*** Compra de snacks con funciones ***')
lista_snacks = [
    {
        'Id': 1,
        'Nombre': 'Papas',
        'Precio': 15
       
    },
    {
        'Id': 2,
        'Nombre': 'Refresco',
        'Precio': 18
    },
    {
        'Id': 3,
        'Nombre': 'Sndwich',
        'Precio': 20
    }
]
lista_compra = []

def mostrar_productos():
    print('---Snacks Disponibles---')
    for producto in lista_snacks:
        print(f'Id: {producto.get('Id')} -> {producto.get('Nombre')} - {producto.get('Precio')}')

def compra_snacks(id_input):
    if id_input.isdigit():
        id_elegido = int(id_input)
    else:
        print('Ingrese únicamente números')
        return
    producto_comprado = None
   
    for snack in lista_snacks:
        if snack.get('Id') == id_elegido:
            producto_comprado = snack
            lista_compra.append(producto_comprado)
            print(f'{producto_comprado.get('Nombre')} agregado al carrito')
           
            print('\n--- Carrito completo ---')
            for producto in lista_compra:
                print(f"- {producto.get('Nombre')} - ${producto.get('Precio')}")
            print(f'Total de productos: {len(lista_compra)}')
            return
    print(f'El producto con ID {id_elegido} no se encontró')
   
def mostrar_ticket():
    if not lista_compra:
        print('No tienes productos en tu carrito')
        return
    print('---Ticket de compra---')
   
    subtotal = 0
   
    for producto in lista_compra:
        nombre = producto.get('Nombre')
        precio = producto.get('Precio')
       
        subtotal += precio
       
        print(f'- {nombre} - ${precio}')
    print(f'TOTAL -> {subtotal}')
       
while True:
    print('\n----Menú----')
    print('1.- Mostrar lista de snacks')
    print('2.- Comprar Snacks')
    print('3.- Mostrar ticket')
    print('4.- Salir')
   
    opcion = input('Elige una opción: ')
   
    if opcion == '1':
        mostrar_productos()
    elif opcion == '2':
        id_snack = input('Ingresa el ID del snack que deseas comprar: ')
        compra_snacks(id_snack)
    elif opcion == '3':
        mostrar_ticket()
    elif opcion == '4':
        print('Saliendo del sistema ...')
        break
    else:
        print('Elige una opción válida')
    