'''
Crear un inventario de productos de tal manera que se almacenen
la información de cada uno de ellos en un diccionario y todos los
diccionarios se almacenen en una lista. Cada producto debe tener id,
nombre, precio y cantidad. Pedir al usuario el número de productos 
a almacenar.
'''
print('*** Inventario de Productos ***')

inventario_Productos = []
cantidad_productos = int(input('Ingresa el # de productos en el inventario: '))

for i in range(cantidad_productos):
    print(f'\nProducto #({i+1})')
    nombre = input('Nombre del prodcto: ')
    precio = float(input('Precio del producto: '))
    cantidad = int(input('Cantidad de productos: '))
    
    producto = {
        'Id': i +1,
        'Nombre': nombre,
        'Precio': precio,
        'Cantidad': cantidad
    }
    inventario_Productos.append(producto)
    
print('\nProductos en el inventario:')
for i, producto in enumerate(inventario_Productos):
    print(f'''
        Producto #{i+1}
        Id: {producto.get('Id')}
        Nombre: {producto.get('Nombre')}
        Precio: {producto.get('Precio')}
        Cantidad: {producto.get('Cantidad')}
        ''')
print('\nBúsqueda de productos en el inventario:')
id_busqueda = int(input('Ingrese el ID del producto a buscar: '))

producto_encontrado = None
for producto in inventario_Productos:
    if producto.get('Id') == id_busqueda:
        producto_encontrado = producto
        break
if producto_encontrado:
    print(f'\nProducto encontrado:\n'
          f'Id: {producto_encontrado.get("Id")}\n'
          f'Nombre: {producto_encontrado.get("Nombre")}\n'
          f'Precio: {producto_encontrado.get("Precio")}\n'
          f'Cantidad: {producto_encontrado.get("Cantidad")}')
else:
    print(f'\nProducto con ID {id_busqueda} no encontrado en el inventario.')


