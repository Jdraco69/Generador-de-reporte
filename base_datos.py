import mysql.connector
from mysql.connector import Error

def mostrar_por_fecha(fecha_inicio, fecha_fin):
     cursor = connection.cursor()
     cursor.execute("SELECT id,nombre,tipo,precio FROM ventas Where date_time >= %s and date_time<= %s", (fecha_inicio, fecha_fin))    
     results = cursor.fetchall()
     for row in results:
         print(row)

#esta es una funcion temporal para probar el sistema de fechas
def fecha_prueba():
    dia_1 = input("Ingrese el dia de la primera fecha: ")
    mes_1 = input("Ingrese el mes de la primera fecha: ")
    año_1 = input("Ingrese el año de la primera fecha: ")
    Primera_fecha = f"{año_1}-{mes_1}-{dia_1}"
    print(f"Fecha de inicio: {Primera_fecha}")
    dia_2 = input("Ingrese el dia de la segunda fecha: ")  
    mes_2 = input("Ingrese el mes la segunda fecha: ")
    año_2 = input("Ingrese el año la segunda fecha: ") 
    segunda_fecha = f"{año_2}-{mes_2}-{dia_2}"
    print(f"segunda fecha :{segunda_fecha}")
    return Primera_fecha, segunda_fecha
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
        fris_date ,secon_dates =fecha_prueba()
        mostrar_por_fecha(fris_date ,secon_dates)

except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

