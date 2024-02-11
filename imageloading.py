import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('water_meter.png')

resized_image = cv2.resize(image, None, fx=0.5, fy=0.5)

# Convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
morph_image = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

# Thresholding
_, threshold_image = cv2.threshold(morph_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Use Tesseract to extract text from the thresholded image
extracted_text = pytesseract.image_to_string(threshold_image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)