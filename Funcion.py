from datetime import datetime
from dateutil import parser
import os
import pandas as pd

def ingresar_fecha():
    
    while True:
        try:
            print("\n--- Ingreso de Fechas ---")
            print("Formato aceptado: dd/mm/yy")
            
            str_inicio = input("Fecha de inicio: ").strip()
            str_fin = input("Fecha de fin: ").strip()
            
            
            fecha_inicio = parser.parse(str_inicio).date()
            fecha_fin = parser.parse(str_fin).date()
            
            
            if fecha_inicio > fecha_fin:
                print("\n¡Error! La fecha de inicio no puede ser posterior a la fecha de fin.")
                continue
              
            
            hoy = datetime.now().date()
            if fecha_inicio > hoy or fecha_fin > hoy:
                print("\n¡Advertencia! Estás ingresando fechas futuras.")
                confirm = input("¿Continuar? (s/n): ").lower()
                if confirm != 's':
                    continue
                       
            return fecha_inicio, fecha_fin
            
        except ValueError as e:
            print(f"\n¡Error! Fecha no válida: {e}")
            print("Por favor, ingresa las fechas nuevamente.\n")
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Intenta nuevamente.\n")
            
def exportar_a_excel(df, archivo_excel,f1,f2):
    """Exporta el DataFrame a una nueva hoja en el archivo Excel"""
    if df is None or df.empty:
        print("No hay datos para exportar")
        return False
    
    try:
        # Obtener el número de reporte
        nombre_hoja = f"reporte_{f1}al_{f2}"
        
        # Configurar el motor de escritura
        if os.path.exists(archivo_excel):
            mode = 'a'  # Append si el archivo existe
        else:
            mode = 'w'  # Write si no existe
            
        with pd.ExcelWriter(
            archivo_excel,
            engine='openpyxl',
            mode=mode,
            if_sheet_exists='replace'  # Reemplazar si la hoja ya existe
        ) as writer:
            df.to_excel(writer, sheet_name=nombre_hoja, index=False)

            # Ajustar automáticamente el ancho de las columnas
            worksheet = writer.sheets[nombre_hoja]
            for column in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in column)
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[column[0].column_letter].width = adjusted_width
        
        print(f"Datos exportados correctamente a la hoja '{nombre_hoja}' en '{archivo_excel}'")
        return True
        
    except Exception as e:
        print(f"Error al exportar a Excel: {e}")
        return False
            