print('*** SISTEMA DE INVENTARIOS CON FUNCIONES ***')

inventario = []

def agregar_producto(inventario, cant_prod):
    for i in range(cant_prod):
        print(f'Producto #{len(inventario)+1}')
        nombre = input('Ingrese el nombre del producto: ')
        precio = float(input('Ingrese el precio del producto: '))
        cantidad = int(input('Ingrese la cantidad disponible: '))
        
        producto = {
            'Id': len(inventario) + 1,
            'Nombre': nombre,
            'Precio': precio,
            'Cantidad': cantidad
        }
        inventario.append(producto)
    return inventario

def mostrar_productos(inventario):
    if not inventario:
        print('¡El inventario está vacío!')
    else:
        for i, producto in enumerate(inventario):
            print(f'''Producto #{i + 1}
Id: {producto.get('Id')}
Nombre: {producto.get('Nombre')}
Precio: {producto.get('Precio')}
Cantidad: {producto.get('Cantidad')}
''')

def buscar_producto(inventario, id_input):
    if id_input.isdigit():
        id_buscado = int(id_input)
    else:
        print('Ingrese únicamente números')
        return
    producto_encontrado = None
    
    for producto in inventario:
        if producto.get('Id') == id_buscado:
            producto_encontrado = producto
            break
    if producto_encontrado:
        print(f'''Producto encontrado:
Id: {producto_encontrado.get('Id')}
Nombre: {producto_encontrado.get('Nombre')}
Precio: {producto_encontrado.get('Precio')}
Cantidad: {producto_encontrado.get('Cantidad')}
''')
    else:
        print(f'No se encontró producto con el Id {id_buscado}')

def borrar_producto(inventario, id_usuario):
    if id_usuario.isdigit():
        id_buscado = int(id_usuario)
    else:
        print('Ingrese únicamente números')
        return
    for i, producto in enumerate(inventario):
        if producto.get('Id') == id_buscado:
            print(f'El producto encontrado es: {producto.get("Nombre")}')
            
            confirmación = input('¿Desea eliminar este producto del inventario? (si/no): ')
            if confirmación.lower() == 'si':
                inventario.pop(i)
                print(f'Producto con Id {id_buscado} eliminado')
            else:
                print('Se ha cancelado la operación')
            return
    print(f'No se encontró producto con Id {id_buscado}')


# Menú principal
while True:
    print("\n--- Menú de opciones ---")
    print("1. Agregar productos")
    print("2. Mostrar inventario")
    print("3. Buscar producto por ID")
    print("4. Eliminar producto por ID")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        try:
            cant = int(input("¿Cuántos productos desea agregar?: "))
            agregar_producto(inventario, cant)
        except ValueError:
            print("Debe ingresar un número entero para la cantidad.")
    
    elif opcion == '2':
        mostrar_productos(inventario)

    elif opcion == '3':
        id_input = input("Ingrese el ID del producto a buscar: ")
        buscar_producto(inventario, id_input)

    elif opcion == '4':
        id_input = input("Ingrese el ID del producto a eliminar: ")
        borrar_producto(inventario, id_input)

    elif opcion == '5':
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Por favor, seleccione del 1 al 5.")
