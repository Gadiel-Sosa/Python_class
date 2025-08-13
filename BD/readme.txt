Para esta parte se trabajará con PostgreSQL para manejar bases de datos, ya que es una herrameinta que trabaja muy bien con Python.

CONSULTAS BÁSICAS:
SELECT * FROM nombre_tabla WHERE condición --> para consultas específicas
--INSERTAR VALORES A LA TABLA
INSERT INTO nombre_tabla(columna1, columna2, columna3) VALUES(valor1, valor2, valor3) --> para valores de tipo string se usan ''
SELECT * FROM nombre_tabla --> para mostrar todos los valores de la tabla
ACTUALIZAR VALORES DE LA TABLA 
--UPDATE nombre_tabla SET columna1 = valor_nuevo, columna2 = valor_nuevo WHERE condición 
--ELIMINAR UN REGISTRO
--DELETE FROM nombre_tabla WHERE condición

PARA TRABAJAR CON ESTA BD SE DEVE DE CREAR UN ENTORNO VIRTUAL CON 
python -m venv venv --> DENTRO DE TU CARPETE PROYECTO
venv\Scripts\activate --> ACTIVALO
pip install psycopg2 --> DESCARGAS EL MÓDULO PARA TRABAJAR CON PostgreSQL
