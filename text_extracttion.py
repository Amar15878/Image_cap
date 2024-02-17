from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"Error: {e}")
        return None

image_path = "Image1.jpg"
extracted_text = extract_text_from_image(image_path)
if extracted_text:
    print("Extracted Text:")
    print(extracted_text)