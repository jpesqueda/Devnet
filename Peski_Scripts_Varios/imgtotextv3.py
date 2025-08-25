import cv2
import pytesseract
import os
from PIL import Image
import numpy as np

###  este es el mero chido
# Especificar la ruta de Tesseract manualmente
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract\tesseract.exe"

# Función para preprocesar la imagen y mejorar la precisión de OCR
def preprocesar_imagen(imagen_path):
    # Leer la imagen
    imagen = cv2.imread(imagen_path)
    
    if imagen is None:
        return None  # Si la imagen no se puede leer, devolver None
    
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un umbral (thresholding) para mejorar la visibilidad del texto
    _, umbralizada = cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY)
    
    return umbralizada

# Función principal para extraer texto de imágenes
def extraer_texto_de_imagenes():
    # Solicitar al usuario la ruta donde están las imágenes
    ruta_imagenes = input("Introduce la ruta de la carpeta con las imágenes: ").strip()
    
    if not os.path.isdir(ruta_imagenes):
        print("❌ La ruta no es válida. Verifica la carpeta.")
        return

    # Crear una carpeta IMGTOTEXT para guardar el archivo de texto
    carpeta_salida = os.path.join(ruta_imagenes, "IMGTOTEXT")
    os.makedirs(carpeta_salida, exist_ok=True)

    # Solicitar el nombre del archivo de salida
    nombre_archivo = input("Introduce el nombre del archivo de texto (sin extensión): ").strip()
    ruta_salida = os.path.join(carpeta_salida, f"{nombre_archivo}.txt")

    # Obtener la lista de imágenes
    archivos = [f for f in os.listdir(ruta_imagenes) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))]

    if not archivos:
        print("❌ No se encontraron imágenes en la carpeta.")
        return
    
    # Abrir el archivo de salida para guardar los resultados
    with open(ruta_salida, 'w') as archivo_salida:
        for imagen_nombre in archivos:
            imagen_path = os.path.join(ruta_imagenes, imagen_nombre)
            print(f"🖼️ Procesando imagen: {imagen_nombre}")
            
            # Preprocesar la imagen
            imagen_procesada = preprocesar_imagen(imagen_path)
            
            if imagen_procesada is None:
                print(f"⚠️ No se pudo procesar la imagen {imagen_nombre}.")
                archivo_salida.write(f"⚠️ No se pudo procesar la imagen {imagen_nombre}.\n")
                continue
            
            # Extraer texto utilizando pytesseract
            try:
                texto = pytesseract.image_to_string(imagen_procesada, lang="eng")
                if texto.strip():  # Solo agregar texto no vacío
                    archivo_salida.write(f"\nTexto de {imagen_nombre}:\n")
                    archivo_salida.write(texto)
                    archivo_salida.write("\n\n" + "-"*50 + "\n")
                    print(f"✅ Texto extraído de {imagen_nombre}.")
                else:
                    archivo_salida.write(f"\nTexto no encontrado en {imagen_nombre}.\n")
            except Exception as e:
                print(f"⚠️ Error al procesar {imagen_nombre}: {e}")
                archivo_salida.write(f"⚠️ Error al procesar {imagen_nombre}: {e}\n")

    print(f"\n🎉 Proceso completado. El archivo de texto se ha guardado en: {ruta_salida}")

# Ejecutar la función principal
if __name__ == "__main__":
    extraer_texto_de_imagenes()