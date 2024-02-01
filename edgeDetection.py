import cv2
import matplotlib.pyplot as plt
#Load an image from file
image_path = r'C:\Users\uwrma\OpenCV\lena.jpg'
image = cv2.imread(image_path)
#Apply Canny edge detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 50, 150)
#Display the edges
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection')
plt.show()