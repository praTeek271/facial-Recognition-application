import cv2
import numpy as np

# Load the model
model = cv2.dnn.readNetFromTensorflow("path/to/revnet.pb")

# Define the input and output layers
input_layer = "input"
output_layer = "output"

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get the next frame
    ret, frame = cap.read()
    
    # Convert the frame to a 4D blob
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    
    # Pass the blob through the model
    model.setInput(blob)
    output = model.forward()
    
    # Get the index of the highest confidence
    index = np.argmax(output)
    
    # Draw the bounding box around the face
    x, y, w, h = output[index][3:]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show the frame
    cv2.imshow("Face Detection", frame)
    
    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
