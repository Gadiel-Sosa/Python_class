class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente_dato = 0
class Cola:
    def __init__(self):
        self.frente_cola = 0
        self.final_cola = 0
        self.tamaño = 0
    def tamaño_cola(self):
        return self.tamaño
    def cola_vacia(self):
        return self.frente_cola == 0
    def ver_frente_cola(self):
        if self.cola_vacia():
            return 'La cola está vacía'
        return self.frente_cola.dato
    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cola_vacia():
            self.frente_cola = nuevo_nodo
            self.final_cola = nuevo_nodo
        else:
            self.final_cola.siguiente_dato = nuevo_nodo
            self.final_cola = nuevo_nodo
        self.tamaño += 1
    def desencolar(self):
        if self.cola_vacia():
            return "La cola está vacía"
        dato = self.frente_cola.dato
        self.frente_cola = self.frente_cola.siguiente_dato
        if self.frente_cola == 0:
            self.final_cola = 0
        self.tamaño -= 1
        return dato
    def mostrar_cola(self):
        if self.cola_vacia():
            print("La cola está vacía.")
        else:
            actual = self.frente_cola
            while actual != 0:
                actual.dato.imprimir()
                actual = actual.siguiente_dato
class Pedido:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente
        self.cantidad = cantidad
    def imprimir(self):
        """Imprime la información del pedido."""
        print(f"     Cliente: {self.cliente}")
        print(f"     Cantidad: {self.cantidad}")
        print("     ------------")
cola_pedidos = Cola()

pedido1 = Pedido(5, "Juan Pérez")
pedido2 = Pedido(10, "Ana García")
pedido3 = Pedido(3, "Carlos López")

cola_pedidos.encolar(pedido1)
cola_pedidos.encolar(pedido2)
cola_pedidos.encolar(pedido3)

cola_pedidos.mostrar_cola()

print("Pedido desencolado:")
pedido_desencolado = cola_pedidos.desencolar()
pedido_desencolado.imprimir()

cola_pedidos.mostrar_cola()
