
nombre_completo = "Gadiel Antonio Sosa Chan"
print(f'Usuario: {nombre_completo}')
nombre_usuario = nombre_completo.strip()
nombre_usuario = nombre_usuario.replace(' ', '.')
nombre_usuario = nombre_usuario.lower()

nombre_empresa = 'Tecnologico Merida'
print(f'nombre empresa: {nombre_empresa}')
nombre_institucion = nombre_empresa.strip()
nombre_institucion = nombre_institucion.lower()
nombre_institucion =nombre_institucion.replace(' ','')

concatenar_datos = nombre_usuario + '@' + nombre_institucion + '.com.mx'

print(f'E-mail final: {concatenar_datos}')