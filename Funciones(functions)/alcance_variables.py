print('*** Alcance de variables ***')

contador_global = 0

def incrementar_contador():
    # declarar variable local
    contador_local = 0
    # usar variable global
    global contador_global
    contador_global += 1
    contador_local += 1
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

print(f'Valor de la variable global: {contador_global}')