print("*** Ssitema prestamo libros ***")
DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante? (Si/No): ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_por_credencial = (tiene_credencial.lower().strip() == 'si' or
                              distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)
print('Eres elegible para préstamo de libros? ',es_elegible_por_credencial)


