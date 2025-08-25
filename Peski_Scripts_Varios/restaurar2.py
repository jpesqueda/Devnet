import os
import cv2
import torch
import requests
import numpy as np
from PIL import Image
from basicsr.archs.rrdbnet_arch import RRDBNet
from gfpgan import GFPGANer

def descargar_modelo():
    modelo_url = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.8/GFPGANv1.3.pth"
    modelo_path = "GFPGANv1.3.pth"
    
    if not os.path.exists(modelo_path):
        print("Descargando modelo GFPGAN...")
        try:
            response = requests.get(modelo_url, stream=True)
            response.raise_for_status()  # Asegura que la descarga fue exitosa
            with open(modelo_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Modelo descargado.")
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar el modelo: {e}")
            return None
    return modelo_path

def restaurar_imagen(ruta_imagen):
    modelo_path = descargar_modelo()
    if modelo_path is None:
        return
    
    dispositivo = 'cuda' if torch.cuda.is_available() else 'cpu'
    gfpgan = GFPGANer(model_path=modelo_path, upscale=2, arch='clean', channel_multiplier=2, bg_upsampler=None, device=dispositivo)
    
    # Cargar imagen usando OpenCV (en formato BGR)
    img = cv2.imread(ruta_imagen, cv2.IMREAD_COLOR)
    if img is None:
        print("Error: No se pudo cargar la imagen. Verifique la ruta.")
        return
    
    # Procesar la imagen
    _, restored_img = gfpgan.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
    
    # Guardar la imagen restaurada
    directorio, nombre_archivo = os.path.split(ruta_imagen)
    nombre_base, extension = os.path.splitext(nombre_archivo)
    ruta_salida = os.path.join(directorio, f"{nombre_base}_restaurada{extension}")
    
    # Escribir imagen restaurada
    cv2.imwrite(ruta_salida, restored_img)
    print(f"Imagen restaurada guardada en: {ruta_salida}")

if __name__ == "__main__":
    ruta_imagen = input("Ingrese la ruta completa de la imagen dañada: ")
    restaurar_imagen(ruta_imagen)
