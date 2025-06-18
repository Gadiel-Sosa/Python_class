from idlelib.replace import replace

nombre_usuario = input('Introduce tus nombres: ').strip().lower()
apellidos_usuario = input('Introduce tus apellidos: ').strip().lower()
nombre_institucion = input('Introduece el nombre de tu institución: ').strip().lower()
dominio = input('Introduce el dominio por ejemplo (.com.mx): ').strip().lower().replace(' ','')
caracter_especial = '@'

nombre_usuario_e = nombre_usuario.replace(' ','.')
apellidos_usuario_e = apellidos_usuario.replace(' ','.')
nombre_institucion_e = nombre_institucion.replace(' ','')

e_mail = f'{nombre_usuario_e}.{apellidos_usuario_e}{caracter_especial}{nombre_institucion_e}{dominio}'
print(f'E-Mail generado: {e_mail}')