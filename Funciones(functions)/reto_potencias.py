print('*** Potencias con recursividad ***')
# Caso nase es que b sea 0 a^b si es 0 entonces es 1
def potencia_recursiva(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia_recursiva(a, b-1)
print(potencia_recursiva(2,190))