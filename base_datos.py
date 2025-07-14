import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="",
        database="proyecto_informe"
    )
    if connection.is_connected():
        print("Conexión exitosa a la base de datos")
        info = connection.get_server_info()
        print(f"Versión del servidor MySQL: {info}")

except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")