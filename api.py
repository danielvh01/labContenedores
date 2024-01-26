import mysql.connector

def conectar():
    # Configuración de la conexión a MySQL
    config = {
        'user': 'root',
        'password': 'wordpress',
        'host': 'localhost',
        'database': 'wordpress',
        'port': 3306
    }

    # Conectar a la base de datos
    conexion = mysql.connector.connect(**config)

    return conexion

def cerrar_conexion(conexion, cursor):
    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()

def insertar_participante(cursor, nombre, carne):
    # Consulta SQL de inserción
    consulta = "INSERT INTO participante (nombre, carne) VALUES (%s, %s)"

    # Datos a insertar
    datos = (nombre, carne)

    try:
        # Ejecutar la consulta
        cursor.execute(consulta, datos)

        # Confirmar la transacción
        conexion.commit()

        print("Inserción exitosa")

    except mysql.connector.Error as error:
        # En caso de error, realizar rollback
        conexion.rollback()
        print(f"Error al insertar: {error}")

def actualizar_participante(cursor, id_participante, nuevo_nombre, nueva_carne):
    # Consulta SQL de actualización
    consulta = "UPDATE participante SET nombre = %s, carne = %s WHERE id = %s"

    # Datos para la actualización
    datos = (nuevo_nombre, nueva_carne, id_participante)

    try:
        # Ejecutar la consulta
        cursor.execute(consulta, datos)

        # Confirmar la transacción
        conexion.commit()

        print("Actualización exitosa")

    except mysql.connector.Error as error:
        # En caso de error, realizar rollback
        conexion.rollback()
        print(f"Error al actualizar: {error}")

def eliminar_participante(cursor, id_participante):
    # Consulta SQL de eliminación
    consulta = "DELETE FROM participante WHERE id = %s"

    # Datos para la eliminación
    datos = (id_participante,)

    try:
        # Ejecutar la consulta
        cursor.execute(consulta, datos)

        # Confirmar la transacción
        conexion.commit()

        print("Eliminación exitosa")

    except mysql.connector.Error as error:
        # En caso de error, realizar rollback
        conexion.rollback()
        print(f"Error al eliminar: {error}")

# Conectar a la base de datos
conexion = conectar()

try:
    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Datos para la inserción
    nombre_insertar = 'Juan'
    carne_insertar = 1120020

    # Insertar un nuevo participante
    insertar_participante(cursor, nombre_insertar, carne_insertar)

    # Obtener el ID del participante recién insertado
    id_participante_insertado = cursor.lastrowid

    # Datos para la actualización
    nuevo_nombre_actualizar = 'Juan Actualizado'
    nueva_carne_actualizar = 1120021

    # Actualizar el participante recién insertado
    actualizar_participante(cursor, id_participante_insertado, nuevo_nombre_actualizar, nueva_carne_actualizar)

    # Datos para la eliminación
    id_participante_eliminar = id_participante_insertado

    # Eliminar el participante recién insertado y actualizado
    eliminar_participante(cursor, id_participante_eliminar)

finally:
    # Cerrar cursor y conexión al finalizar
    cerrar_conexion(conexion, cursor)
