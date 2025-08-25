#convieerte gors a pedefe
#peskipolla
#pip install python-docx
#jalandin al ciego apa, si usalo esta mamalon 


import os
import sys
from pathlib import Path
from docx import Document
from reportlab.pdfgen import canvas

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        # Open the Word document
        doc = Document(docx_path)
        # Create a PDF canvas
        pdf = canvas.Canvas(pdf_path)

        # Write each paragraph in the Word document to the PDF
        y_position = 800
        for para in doc.paragraphs:
            if y_position < 50:
                pdf.showPage()
                y_position = 800
            pdf.drawString(50, y_position, para.text)
            y_position -= 14

        pdf.save()
        print(f"Converted: {docx_path} -> {pdf_path}")

    except Exception as e:
        print(f"Error converting {docx_path}: {e}")


def main():
    folder_path = input("Ingrese la ruta de la carpeta: ").strip()

    if not os.path.exists(folder_path):
        print("Error: La ruta especificada no existe.")
        sys.exit(1)

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".docx"):
            docx_path = os.path.join(folder_path, file_name)
            pdf_path = os.path.join(folder_path, Path(file_name).stem + ".pdf")
            convert_docx_to_pdf(docx_path, pdf_path)

if __name__ == "__main__":
    main()
