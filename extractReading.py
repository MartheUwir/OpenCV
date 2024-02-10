import pytesseract
from PIL import Image


# Set the path to the Tesseract executable (update the path accordingly)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)

    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

    return text

# Provide the path to your image
image_path = r'C:\Users\uwrma\OpenCV\second.png'

# Extract text from the image
result_text = extract_text_from_image(image_path)

# Print the extracted text
print("Extracted Text:")
print(result_text)
