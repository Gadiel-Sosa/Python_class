print('*** Combinación listas y tuplas')
productos = [
    ('P001', 'Camiseta', 20.0),
    ('P002', 'Jeans', 30.0),
    ('P003', 'Sudadera', 40.0)
]

precio_total = 0
print('Información de los productos: ')
for producto in productos:
    id, descripcion, precio = producto
    print(f'producto: id = {id}, descripción = {descripcion}, precio = {precio}')
    precio_total += precio
print(f'Precio total de los productos: {precio_total}')
