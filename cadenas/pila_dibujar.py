# Inicializar la pila y el puntero al tope
pila = []
tope = 0
tamaño_maximo = 8

# Función para dibujar la pila con texto gráfico
def dibujar_pila_texto():
    print("\nEstado actual de la pila:")
    for i in range(tamaño_maximo - 1, -1, -1):
        if i < tope:
            print(f"|  {pila[i]}  |  <-- Posición {i+1}")
        else:
            print(f"|     |  <-- Posición {i+1}")
    print(" ------ ")
    print(f"Tope actual: {tope}\n")

# Función para insertar un elemento en la pila
def insertar(elemento):
    global tope
    if tope < tamaño_maximo:
        pila.append(elemento)
        tope += 1
        print(f"Insertado: {elemento}")
    else:
        print("Error: La pila está llena")
    dibujar_pila_texto()

# Función para eliminar un elemento de la pila
def eliminar():
    global tope
    if tope > 0:
        eliminado = pila.pop()
        tope -= 1
        print(f"Eliminado: {eliminado}")
    else:
        print("Error: La pila está vacía")
    dibujar_pila_texto()

# Estado inicial de la pila
dibujar_pila_texto()

# Operaciones
insertar("X")
insertar("Y")
eliminar()
eliminar()
eliminar()  # Intento de subdesbordamiento
insertar("V")
insertar("W")
eliminar()
insertar("R")
