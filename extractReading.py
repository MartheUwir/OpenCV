import cv2
import pytesseract

# Path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'C:\Users\uwrma\OpenCV\lena.jpg'

def read_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(gray_image)

    return text

if __name__ == "__main__":
    # Image file path (assuming 'lena.jpg' is in the same folder)
    image_path = 'lena.jpg'

    # Read text from the image
    result_text = read_image(image_path)

    # Print the extracted text
    print("Text extracted from the image:")
    print(result_text)
