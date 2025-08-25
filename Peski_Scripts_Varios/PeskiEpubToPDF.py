#pip install ebooklib reportlab
#pip install beautifulsoup4
#peskipolla
#jala de la perca no lo uses mi peki

import os
import sys
from ebooklib import epub
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup

# Función para convertir EPUB a PDF
def convert_epub_to_pdf(epub_path, pdf_path):
    try:
        # Cargar el archivo EPUB
        book = epub.read_epub(epub_path)
        pdf = canvas.Canvas(pdf_path, pagesize=LETTER)
        width, height = LETTER
        y_position = height - 40
        margin = 40
        line_height = 14

        # Iterar sobre los elementos del EPUB
        for item in book.get_items():
            # Verificar si el elemento es HTML
            if isinstance(item, epub.EpubHtml):
                try:
                    content = item.get_body_content()
                    soup = BeautifulSoup(content, 'html.parser')
                    text = soup.get_text()
                    lines = text.splitlines()

                    for line in lines:
                        line = line.strip()
                        if line:
                            if y_position < margin:
                                pdf.showPage()
                                y_position = height - 40
                            pdf.drawString(margin, y_position, line)
                            y_position -= line_height
                except Exception as e:
                    print(f"Error al procesar un elemento EPUB: {e}")

        pdf.save()
        print(f"Archivo PDF generado correctamente en: {pdf_path}")
    except Exception as e:
        print(f"Error al convertir EPUB a PDF: {e}")

# Función principal
def main():
    epub_path = input("Ingrese la ruta completa del archivo EPUB: ").strip()
    if not os.path.isfile(epub_path):
        print("El archivo especificado no existe. Verifique la ruta e intente nuevamente.")
        sys.exit(1)

    pdf_path = os.path.splitext(epub_path)[0] + ".pdf"
    convert_epub_to_pdf(epub_path, pdf_path)

if __name__ == "__main__":
    main()
