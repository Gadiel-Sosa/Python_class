import psycopg2
# Importa la librería psycopg2, que es el conector para trabajar con bases de datos PostgreSQL desde Python.

conexion = psycopg2.connect(
    user = 'postgres',          # Usuario para conectarse a la base de datos PostgreSQL.
    password = 'admin',         # Contraseña del usuario.
    host = '127.0.0.1',         # Dirección del servidor donde está la base de datos (localhost en este caso).
    port = '5432',              # Puerto por donde PostgreSQL escucha (por defecto es 5432).
    database = 'test_db'        # Nombre de la base de datos a la que queremos conectarnos.
)
# Esta línea crea una conexión con la base de datos usando los parámetros dados. Si algo falla (credenciales, servidor, etc.), lanzará un error.

cursor = conexion.cursor()
# Crea un cursor, que es un objeto que nos permite ejecutar comandos SQL dentro de la conexión.

sentencia = 'SELECT * FROM persona'
# Aquí definimos una consulta SQL que selecciona todos los registros de la tabla "persona".

cursor.execute(sentencia)
# Ejecuta la consulta SQL a través del cursor.

registros = cursor.fetchall()
# Obtiene todos los resultados de la consulta y los guarda en la variable 'registros'. Es una lista de tuplas, cada tupla representa una fila de la tabla.

print(registros)
# Imprime la lista completa de registros obtenidos.

cursor.close()
# Cierra el cursor para liberar recursos.

conexion.close()
# Cierra la conexión con la base de datos para liberar recursos y evitar bloqueos.
