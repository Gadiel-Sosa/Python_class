class Producto:
    contador_producto = 0
    def __init__(self,nombre, cantidad, precio_unitario):
        Producto.contador_producto += 1
        self.id_prod = Producto.contador_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
    
    def __str__(self):
        return f'ID: {self.id_prod}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio unitario: {self.precio_unitario}'
 
        