import pandas as pd  
import mysql.connector
from mysql.connector import Error

def obtener_ventas_por_fecha():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user="root",
            password="",
            database="proyecto_informe"
        )
        fecha_inicio="2025-06-28"
        fecha_fin="2025-07-01"

        
        query = "SELECT id,nombre,tipo,precio,fecha FROM ventas Where fecha >= %s and fecha<= %s"  
        
        
        dataframe = pd.read_sql(query, connection,params=(fecha_inicio, fecha_fin))
        
        print(dataframe)
        return dataframe
        
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    df = obtener_ventas_por_fecha()
    if df is not None:
        df.to_excel("ventas_por_fecha3.xlsx", index=False)
        print("Datos exportados a ventas_por_fecha.xlsx")