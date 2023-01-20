import cv2
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.models import load_model
import numpy as np

# Load the pre-trained model
model = ResNet50(weights="imagenet")

# Load the violence detection model
violence_model = load_model("violence_detection.h5")

# Set up the camera
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the camera
    ret, frame = cap.read()

    # Resize the frame to the required input size for ResNet50
    frame = cv2.resize(frame, (224, 224))
    frame = img_to_array(frame)
    frame = np.expand_dims(frame, axis=0)
    frame = imagenet_utils.preprocess_input(frame)

    # Pass the frame through ResNet50
    features = model.predict(frame)

    # Pass the features through the violence detection model
    preds = violence_model.predict(features)

    # Get the class with the highest probability
    label = np.argmax(preds[0])

    # Check if the frame contains violence
    if label == 1:
        print("Violence detected!")
    else:
        print("No violence detected.")

    # Show the frame
    cv2.imshow("Live Video Feed", frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
