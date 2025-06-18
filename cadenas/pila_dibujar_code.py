class Pila:
    def __init__(self, tamaño_maximo=8):
        self.pila = []
        self.tope = 0
        self.tamaño_maximo = tamaño_maximo
    def dibujar_pilas(self):
        print("\nEstado actual de la pila:")
        for i in range(self.tamaño_maximo - 1, -1, -1):
            if i < self.tope:
                print(f"|  {self.pila[i]}  |  <-- Posición {i+1}")
            else:
                print(f"|     |  <-- Posición {i+1}")
        print(" ------ ")
        print(f"Tope actual: {self.tope}\n")
    def insertar(self, elemento):
        if self.tope < self.tamaño_maximo:
            self.pila.append(elemento)
            self.tope += 1
            print(f"Elemento Insertado: {elemento}")
        else:
            print("Error: La pila está llena")
        self.dibujar_pilas()
    def eliminar(self):
        if self.tope > 0:
            eliminado = self.pila.pop()
            self.tope -= 1
            print(f"Elemento Eliminado: {eliminado}")
        else:
            print("Error: La pila está vacía")
        self.dibujar_pilas()
mi_pila = Pila()
mi_pila.dibujar_pilas()

mi_pila.insertar("X")
mi_pila.insertar("Y")
mi_pila.eliminar() #z
mi_pila.eliminar() #T
mi_pila.eliminar() #U
mi_pila.insertar("V")
mi_pila.insertar("W")
mi_pila.eliminar() #P
mi_pila.insertar("R")
