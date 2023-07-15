import cv2
import numpy as np
from numpy import random


# Load the face detection cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the original image
demo = cv2.imread("img4.jpg")
r, c, t = demo.shape

# Create random key
key = random.randint(256, size=(r, c, t))
np.save('key.npy', key)
key1 = np.load('key.npy')

# Encryption and decryption for each face in the image
gray = cv2.cvtColor(demo, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    # Extract the face ROI
    face = demo[y:y+h, x:x+w]

    # Encrypt the face ROI
    encrypted_face = np.zeros((h, w, t), np.uint8)
    for row in range(h):
        for column in range(w):
            for depth in range(t):
                encrypted_face[row, column, depth] = face[row, column, depth] ^ key1[y+row, x+column, depth]

    # Replace the original face ROI with the encrypted one in a copy of the original image
    demo_encrypted = demo.copy()
    demo_encrypted[y:y+h, x:x+w] = encrypted_face

    # Decrypt the encrypted face ROI
    decrypted_face = np.zeros((h, w, t), np.uint8)
    for row in range(h):
        for column in range(w):
            for depth in range(t):
                decrypted_face[row, column, depth] = encrypted_face[row, column, depth] ^ key1[
                    y + row, x + column, depth]

    # Replace the original face ROI with the decrypted one in a copy of the original image
    demo_decrypted = demo.copy()
    demo_decrypted[y:y + h, x:x + w] = decrypted_face
    # Draw the rectangle around the face
    cv2.rectangle(demo, (x, y), (x + w, y + h), (0, 255, 0), 2)


# Display the original image with rectangles around the faces and the encrypted parts
cv2.imshow("Original image with rectangles around the faces and encrypted parts", demo)
cv2.waitKey()

# Display the new image with the encrypted face ROI replaced in the original image
cv2.imshow("New image with encrypted face", demo_encrypted)
cv2.waitKey()
# Display the new image with the decrypted face ROI replaced in the original image
cv2.imshow("New image with decrypted face", demo_decrypted)
cv2.waitKey()

cv2.destroyAllWindows()

