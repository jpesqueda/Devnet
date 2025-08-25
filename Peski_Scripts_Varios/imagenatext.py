import os
import cv2
import pytesseract
from PIL import Image

# Configurar ruta de Tesseract en Windows (modificar según instalación)
# Para Windows, descomenta y ajusta esta línea:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract\tesseract.exe"

def extraer_texto_de_imagenes():
    # Solicitar ruta de carpeta con imágenes
    ruta_carpeta = input("Introduce la ruta de la carpeta con imágenes: ").strip()

    # Verificar si la carpeta existe
    if not os.path.isdir(ruta_carpeta):
        print("❌ La carpeta no existe. Verifica la ruta.")
        return
    
    # Pedir el nombre del archivo de salida
    nombre_archivo = input("Introduce el nombre del archivo de texto de salida (sin extensión): ").strip()
    archivo_salida = f"{nombre_archivo}.txt"

    # Obtener lista de imágenes en la carpeta
    imagenes = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]

    if not imagenes:
        print("❌ No se encontraron imágenes en la carpeta.")
        return

    print(f"🔄 Procesando {len(imagenes)} imágenes...")

    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        for imagen_nombre in imagenes:
            ruta_imagen = os.path.join(ruta_carpeta, imagen_nombre)

            # Cargar imagen con OpenCV
            imagen = cv2.imread(ruta_imagen)

            # Convertir imagen a escala de grises para mejorar OCR
            gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

            # Aplicar OCR con Tesseract
            texto = pytesseract.image_to_string(gris, lang="eng")  # Cambiar "eng" por "spa" para español

            # Guardar resultado en archivo
            archivo.write(f"📄 Imagen: {imagen_nombre}\n")
            archivo.write(texto + "\n" + "-" * 50 + "\n")

            print(f"✅ Texto extraído de {imagen_nombre}")

    print(f"\n📁 Proceso completado. Texto guardado en: {archivo_salida}")

if __name__ == "__main__":
    extraer_texto_de_imagenes()