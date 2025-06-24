print('*** Funciones recursivas ***')
def funcion_recursiva(numero):
    # Caso base: si el número llega a 1
    if numero == 1:
        print(numero, end=' ')
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

funcion_recursiva(5)