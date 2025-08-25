import os
import cv2
import numpy as np

# Función para detectar rayones automáticamente
def detectar_rayones(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar filtro de mediana para reducir ruido
    mediana = cv2.medianBlur(gris, 3)

    # Detectar bordes con Canny
    bordes = cv2.Canny(mediana, 30, 150)

    # Aplicar dilatación para engrosar los bordes detectados
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(bordes, kernel, iterations=1)

    return mask

# Función para restaurar imagen
def restaurar_imagen(imagen, mascara):
    return cv2.inpaint(imagen, mascara, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Pedir al usuario la ruta de la imagen
ruta_imagen = input("Ingrese la ruta de la imagen dañada: ")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifique la ruta e inténtelo de nuevo.")
    exit()

# Detectar rayones automáticamente
mascara_rayones = detectar_rayones(imagen)

# Restaurar imagen
imagen_restaurada = restaurar_imagen(imagen, mascara_rayones)

# Obtener nombre del archivo y directorio
directorio, nombre_archivo = os.path.split(ruta_imagen)
nombre_base, extension = os.path.splitext(nombre_archivo)
nombre_salida = f"{nombre_base}_restaurada{extension}"
ruta_salida = os.path.join(directorio, nombre_salida)

# Guardar la imagen restaurada
cv2.imwrite(ruta_salida, imagen_restaurada)

print(f"Imagen restaurada guardada como: {ruta_salida}")
