# db_connector.py

import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    """
    Clase para gestionar la conexión y las operaciones básicas
    con una base de datos MySQL.
    """
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establece la conexión a la base de datos MySQL."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print(f"[{self.__class__.__name__}] Conexión exitosa a la base de datos '{self.database}'")
                return True
            return False
        except Error as e:
            print(f"[{self.__class__.__name__}] Error al conectar a MySQL: {e}")
            return False

    def disconnect(self):
        """Cierra la conexión a la base de datos MySQL."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print(f"[{self.__class__.__name__}] Conexión a la base de datos cerrada.")

    def fetch_data(self, query, params=None):
        """
        Ejecuta una consulta SELECT y devuelve los resultados.

        Args:
            query (str): La consulta SQL a ejecutar.
            params (tuple, optional): Parámetros para la consulta parametrizada. Defaults to None.

        Returns:
            list: Una lista de tuplas con las filas de resultados, o None si hay un error.
            list: Una lista de nombres de columnas.
        """
        if not self.connection or not self.connection.is_connected():
            print(f"[{self.__class__.__name__}] No hay conexión activa a la base de datos.")
            return None, None

        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            rows = cursor.fetchall()
            # Obtener nombres de columnas
            columns = [i[0] for i in cursor.description]
            return rows, columns
        except Error as e:
            print(f"[{self.__class__.__name__}] Error al ejecutar la consulta: {e}")
            return None, None
        finally:
            if cursor:
                cursor.close()

# Ejemplo de uso (para probar el módulo directamente)
if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'port':'3306',
        'password': "",
        'database': 'proyecto_informe'
    }

    db = MySQLConnector(**db_config)
    if db.connect():
        # Ejemplo: Obtener todos los usuarios
        users_query = "SELECT id, nombre, edad FROM usuarios LIMIT 5;"
        data, cols = db.fetch_data(users_query)

        if data:
            print("\nDatos obtenidos de la base de datos (db_connector):")
            print(cols)
            for row in data:
                print(row)
        else:
            print("No se pudieron obtener datos.")
    db.disconnect()