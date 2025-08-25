import cv2
import numpy as np
import os

# Pedir la ruta de la carpeta con imágenes
ruta_carpeta = input("Introduce la ruta de la carpeta con imágenes: ")

# Verificar si la carpeta existe
if not os.path.isdir(ruta_carpeta):
    print("La carpeta no existe. Verifica la ruta.")
    exit()

# Crear una carpeta de salida
carpeta_salida = os.path.join(ruta_carpeta, "procesadas")
os.makedirs(carpeta_salida, exist_ok=True)

# Obtener lista de imágenes en la carpeta
imagenes = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not imagenes:
    print("No se encontraron imágenes en la carpeta.")
    exit()

print(f"Procesando {len(imagenes)} imágenes...")

for imagen_nombre in imagenes:
    ruta_imagen = os.path.join(ruta_carpeta, imagen_nombre)

    # Cargar imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        print(f"No se pudo cargar la imagen {imagen_nombre}")
        continue

    # Crear una máscara (esto debe ajustarse según la ubicación de la marca de agua)
    mascara = np.zeros(imagen.shape[:2], dtype=np.uint8)
    mascara[50:200, 100:300] = 255  # Ajustar las coordenadas según la marca de agua

    # Aplicar inpainting
    resultado = cv2.inpaint(imagen, mascara, 3, cv2.INPAINT_TELEA)

    # Guardar imagen procesada
    ruta_guardado = os.path.join(carpeta_salida, imagen_nombre)
    cv2.imwrite(ruta_guardado, resultado)

    print(f"Imagen procesada: {imagen_nombre} → Guardada en {ruta_guardado}")

print("Proceso completado.")