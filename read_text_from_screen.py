import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab


# Use pytesseract to read text from an image
def read_text(image_path):
    # Load the image
    
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Use pytesseract to extract the text from the image
    text = pytesseract.image_to_string(gray)
    # Print the extracted text
    print(text)

# Capture the screen using OpenCV
def capture_screen():
    # Get the size of the screen
    screen_size = (1920, 1080)
    # Create a new OpenCV window
    screen = np.array(ImageGrab.grab(bbox=(0,0,screen_size[0],screen_size[1])))
    # Save the screenshot to a file
    cv2.imwrite("screenshot.png", screen)
    # Read the text from the screenshot
    read_text("screenshot.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

capture_screen()
