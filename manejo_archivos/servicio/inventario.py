import csv
import os
class Inventario:
    ruta_archivo = 'inventario.csv'
    @classmethod
    def _agregar_encabezados(cls):
        if not os.path.exists(cls.ruta_archivo):
            with open(cls.ruta_archivo, 'a', newline='', encoding='utf-8') as archivo:
                spawnwriter = csv.writer(archivo)
                spawnwriter.writerow(['ID', 'Nombre', 'Cantidad', 'PrecioU'])
            
    @classmethod
    def agregar_producto(cls, producto):
        cls._agregar_encabezados()
        with open(cls.ruta_archivo, 'a',newline='', encoding='utf-8') as archivo:
            spawnwriter = csv.writer(archivo)
            spawnwriter.writerow([producto.id_prod, producto.nombre, producto.cantidad, producto.precio_unitario])
    @classmethod
    def mostrar_contenido(cls):
        try:
            with open(cls.ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
                reader = csv.reader(archivo)
                next(reader)
                for row in reader:
                    print(f'ID: {row[0]}, Nombre: {row[1]}, Cantidad: {row[2]}, Precio unitario: {row[3]}')
        except Exception as e:
            print(f'Ocurrió un error del tipo: {e}')
    @classmethod
    def buscar_producto(cls, id_buscado):
        try:
            with open(cls.ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
                reader = csv.reader(archivo)
                next(reader)
                for row in reader:
                    if row[0] == str(id_buscado):
                        print(f'''
                            Id: {row[0]}
                            Nombre: {row[1]}
                            Cantidad: {row[2]}
                            Precio unitario: {row[3]}''')
                        return
                print('Producto no encontrado')
        except Exception as e:
            print(f'Ocurrió un error: {e}')
    @classmethod
    def eliminar_inventario(cls):
        try:
            if os.path.exists(cls.ruta_archivo):
                os.remove(cls.ruta_archivo)
                print('El archivo inventario.csv se ha eliminado')
            else:
                print('No se encontró el archivo inventario.csv')
        except Exception as e:
            print(f'Ocurrió un error del tipo: {e}')