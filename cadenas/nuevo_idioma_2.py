def ordenar_palabra(palabra):
    # Ordena los caracteres de una palabra alfabéticamente
    return ''.join(sorted(palabra))

# Captura el número de palabras que contendrá el diccionario
N = int(input('Captura el número de palabras que contendrá el diccionario: '))
diccionario = [input('Introduce la palabra {}: '.format(i + 1)).strip() for i in range(N)]

# Ordenamos las palabras del diccionario, creando una lista de tuplas (palabra_original, palabra_ordenada)
diccionario_ordenado = sorted((palabra, ordenar_palabra(palabra)) for palabra in diccionario)

# Captura el número de consultas
Q = int(input('Captura el número de consultas: '))
consultas = [input('Introduce la consulta {}: '.format(i + 1)).strip() for i in range(Q)]

# Creamos una función para contar y enlistar las palabras que sean menores o iguales a las consultas
def palabras_menores_iguales(diccionario_ordenado, consulta):
    consulta_ordenada = ordenar_palabra(consulta)
    menores_iguales = []
    for original, ordenada in diccionario_ordenado:
        if ordenada <= consulta_ordenada:
            menores_iguales.append((original, ordenada))
    return menores_iguales

# Procesamos cada consulta y mostramos los resultados
for consulta in consultas:
    menores_iguales = palabras_menores_iguales(diccionario_ordenado, consulta)
    total = len(menores_iguales)

    # Mostramos los resultados para cada consulta dentro del bucle
    print(f"\nTotal de palabras menores o iguales que '{consulta}': {total}")
    if total > 0:
        print(f"Palabras menores o iguales que '{consulta}':")
        for original, ordenada in menores_iguales:
            print(f"  - '{original}' (ordenada: '{ordenada}')")
    else:
        print(f"No hay palabras menores o iguales que '{consulta}'.")
