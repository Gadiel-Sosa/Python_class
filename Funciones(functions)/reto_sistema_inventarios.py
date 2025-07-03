print('*** Sistemas de inventarios ***')

inventario = []

def agregar_producto(cantidad_productos):
    for i in range(cantidad_productos):
        print(f'\nProducto #{len(inventario) + 1}')
        nombre = input('Ingresa el nombre del producto: ')
        precio = float(input('Ingresa el precio del producto: '))
        cantidad = int(input('Ingresa la cantidad disponible: '))
        
        producto = {
            'Id': len(inventario) + 1,
            'Nombre': nombre,
            'Precio': precio,
            'Cantidad': cantidad
        }
        inventario.append(producto)
    return inventario

def mostrar_inventario():
    if not inventario:
        print('El inventario está vacío')
    else:
        for i, producto in enumerate(inventario):
            print(f'''
Producto #{i+1}
Id: {producto.get('Id')}
Nombre: {producto.get('Nombre')}
Precio: {producto.get('Precio')}
Cantidad: {producto.get('Cantidad')}
''')

def buscar_producto_por_id(inventario):
    id_input = input('Ingrese el ID del producto a buscar: ')
    
    if not id_input.isdigit():
        print("Error: Debes ingresar un número entero positivo.")
        return

    id_busqueda = int(id_input)
    producto_encontrado = None

    for producto in inventario:
        if producto.get('Id') == id_busqueda:
            producto_encontrado = producto
            break

    if producto_encontrado:
        print(f'''
Producto encontrado:
Id: {producto_encontrado.get("Id")}
Nombre: {producto_encontrado.get("Nombre")}
Precio: {producto_encontrado.get("Precio")}
Cantidad: {producto_encontrado.get("Cantidad")}
''')
    else:
        print(f'\nProducto con ID {id_busqueda} no encontrado en el inventario.')

# Menú interactivo
while True:
    print("\n--- Menú de opciones ---")
    print("1. Agregar productos")
    print("2. Mostrar inventario")
    print("3. Buscar producto por ID")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = input("¿Cuántos productos deseas agregar? ")
        if cantidad.isdigit():
            agregar_producto(int(cantidad))
        else:
            print("Error: Ingresa un número válido.")
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        buscar_producto_por_id(inventario)
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

    
        
        
    

