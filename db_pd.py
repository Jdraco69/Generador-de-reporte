import pandas as pd  
import mysql.connector
from Funcion import ingresar_fecha , exportar_a_excel
from mysql.connector import Error


def db_conneccion():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user="root",
            password="",
            database="proyecto_informe"
        )
        
        fecha_inicio , fecha_fin = ingresar_fecha()
        global f_1, f_2 
        f_1, f_2 = fecha_inicio, fecha_fin
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
    df = db_conneccion()
  
    ARCHIVO_EXCEL = "ventas_excel.xlsx"
  
    # 2. Exportar a Excel
    if  df  is not None:
        if exportar_a_excel( df , ARCHIVO_EXCEL , f_1, f_2):
            print("Proceso completado exitosamente")
        else:
            print("Hubo un problema al exportar los datos")
    else:
        print("No se obtuvieron datos de la base de datos")
