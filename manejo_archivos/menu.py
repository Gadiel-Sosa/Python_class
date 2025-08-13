from dominio.producto import Producto
from servicio.inventario import Inventario
def menu():
    while True:
        print('''
--- Menú Inventario ---
1. Agregar producto
2. Mostrar inventario
3. Buscar producto por ID
4. Eliminar inventario
5. Salir
        ''')

        opcion = input('Selecciona una opción: ')
        
        if opcion == '1':
            nombre = input('Nombre del producto: ')
            cantidad = input('Cantidad: ')
            precio = input('Precio unitario: ')
            try:
                cantidad = int(cantidad)
                precio = float(precio)
                producto = Producto(nombre, cantidad, precio)
                Inventario.agregar_producto(producto)
                print('Producto agregado.')
            except ValueError:
                print('Cantidad debe ser entero y precio debe ser número decimal.')
        
        elif opcion == '2':
            Inventario.mostrar_contenido()
        
        elif opcion == '3':
            id_buscar = input('ID del producto a buscar: ')
            Inventario.buscar_producto(id_buscar)
        
        elif opcion == '4':
            confirmar = input('¿Seguro que quieres eliminar todo el inventario? (s/n): ').lower()
            if confirmar == 's':
                Inventario.eliminar_inventario()
        
        elif opcion == '5':
            print('¡Adiós!')
            break
        
        else:
            print('Opción inválida, intenta otra vez.')

# Asumiendo que ya tienes definida la clase Producto y la clase Inventario
if __name__ == '__main__':
    menu()
