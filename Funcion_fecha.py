from datetime import datetime
from dateutil import parser

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