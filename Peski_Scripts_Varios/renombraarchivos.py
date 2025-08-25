import os

def renombrar_archivos():
    # Pedir la ruta de la carpeta
    ruta_carpeta = input("Introduce la ruta de la carpeta con los archivos: ").strip()

    if not os.path.isdir(ruta_carpeta):
        print("❌ La carpeta no existe. Verifica la ruta.")
        return

    # Pedir el prefijo para los nuevos nombres
    prefijo = input("Introduce el prefijo para los archivos (ejemplo: 'imagen'): ").strip()

    # Obtener lista de archivos
    archivos = sorted([f for f in os.listdir(ruta_carpeta) if os.path.isfile(os.path.join(ruta_carpeta, f))])

    if not archivos:
        print("❌ No se encontraron archivos en la carpeta.")
        return

    print(f"🔄 Renombrando {len(archivos)} archivos...")

    # Renombrar archivos manteniendo la extensión
    for i, archivo in enumerate(archivos, start=1):
        nombre_base, extension = os.path.splitext(archivo)
        nuevo_nombre = f"{prefijo}_{i:03d}{extension}"  # Ejemplo: imagen_001.jpg
        ruta_vieja = os.path.join(ruta_carpeta, archivo)
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        if os.path.exists(ruta_nueva):
            print(f"⚠️ El archivo {ruta_nueva} ya existe. Saltando...")
            continue

        os.rename(ruta_vieja, ruta_nueva)
        print(f"✅ {archivo} → {nuevo_nombre}")

    print("\n🎉 Proceso completado.")

if __name__ == "__main__":
    renombrar_archivos()