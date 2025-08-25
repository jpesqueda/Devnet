import os
import cv2
import numpy as np
import mediapipe as mp

# Inicializar el detector de rostros de Mediapipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Función para detectar rayones y puntos blancos automáticamente
def detectar_defectos(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar filtro de mediana para reducir ruido
    mediana = cv2.medianBlur(gris, 3)

    # Detectar bordes con Canny
    bordes = cv2.Canny(mediana, 30, 150)

    # Detectar áreas blancas anómalas (posibles daños)
    _, blancos = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY)

    # Combinar detecciones
    mask = cv2.bitwise_or(bordes, blancos)

    # Aplicar dilatación para engrosar los bordes detectados
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    return mask

# Función para restaurar imagen
def restaurar_imagen(imagen, mascara):
    return cv2.inpaint(imagen, mascara, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Función para mejorar el tono de la piel
def mejorar_piel(imagen):
    imagen_suavizada = cv2.bilateralFilter(imagen, 15, 75, 75)
    return cv2.addWeighted(imagen, 0.7, imagen_suavizada, 0.3, 0)

# Función para mejorar rostros detectados
def mejorar_rostros(imagen):
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        resultado = face_detection.process(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
        if resultado.detections:
            for detection in resultado.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = imagen.shape
                x, y, ancho, alto = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)
                rostro = imagen[y:y+alto, x:x+ancho]
                imagen[y:y+alto, x:x+ancho] = mejorar_piel(rostro)
    return imagen

# Pedir al usuario la ruta de la imagen
ruta_imagen = input("Ingrese la ruta de la imagen dañada: ")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifique la ruta e inténtelo de nuevo.")
    exit()

# Detectar rayones y puntos blancos automáticamente
mascara_defectos = detectar_defectos(imagen)

# Restaurar imagen
imagen_restaurada = restaurar_imagen(imagen, mascara_defectos)

# Mejorar rostros en la imagen restaurada
imagen_mejorada = mejorar_rostros(imagen_restaurada)

# Obtener nombre del archivo y directorio
directorio, nombre_archivo = os.path.split(ruta_imagen)
nombre_base, extension = os.path.splitext(nombre_archivo)
nombre_salida = f"{nombre_base}_restaurada{extension}"
ruta_salida = os.path.join(directorio, nombre_salida)

# Guardar la imagen restaurada y mejorada
cv2.imwrite(ruta_salida, imagen_mejorada)

print(f"Imagen restaurada y mejorada guardada como: {ruta_salida}")