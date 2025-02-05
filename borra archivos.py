import os

# Solicitar la ruta de la carpeta al usuario
carpeta = input("Ingresa la ruta de la carpeta a limpiar: ")

# Verificar si la carpeta existe
if not os.path.exists(carpeta):
    print("La carpeta no existe. Verifica la ruta e inténtalo de nuevo.")
    exit()

# Definir el tamaño mínimo (10KB = 10240 bytes)
tamaño_minimo = 60 * 1024  

# Recorrer todos los archivos en la carpeta
for archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, archivo)

    # Verificar si es un archivo y su tamaño
    if os.path.isfile(ruta_completa) and os.path.getsize(ruta_completa) < tamaño_minimo:
        print(f"Borrando: {ruta_completa} ({os.path.getsize(ruta_completa)} bytes)")
        os.remove(ruta_completa)  # Eliminar el archivo

print("Proceso completado.")