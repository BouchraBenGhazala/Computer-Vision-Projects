from PIL import Image
import pytesseract

# Si vous ne l'avez pas fait, vous devez installer pytesseract et le lier avec le chemin de votre système
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))  # Nous ouvrons l'image et nous la convertissons en texte
    return text

print(ocr_core('C:/Ensamc/CI/S4/AI/OCR/imageText.png'))  # Remplacez par le chemin de votre image