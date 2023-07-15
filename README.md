
# Images face Detection & Encryptyon-Decryption

this is my gradution project that took me a whole month to finish  
This program utilizes the OpenCV library to detect faces in an image and applies a simple encryption and decryption algorithm to the detected faces. The encrypted faces are replaced with their encrypted versions, providing a visual representation of the encryption process.


## Demo

![](https://github.com/Coffeholic404/Face-Detection-Encryption/blob/main/demo.gif)


## Features

- Loads the Haar cascade classifier for face detection.
- Reads an image file as the input image.
- Generates a random encryption key and saves it.
- Converts the input image to grayscale and detects faces using the cascade classifier.
- For each detected face, it performs encryption and decryption using the generated key.
- Replaces the original face regions with the encrypted and decrypted versions in separate copies of the original image.
- Draws rectangles around the detected faces in the original image.
- Displays the original image with rectangles around the faces and encrypted parts.
- Displays the image with the encrypted face regions replaced in the original image.
- Displays the image with the decrypted face regions replaced in the original image. 


## Installation

Install The following libraries

```python
  pip install opencv-python
  pip install numpy
```
    
## Last Words

This program serves as an educational demonstration of basic face encryption and decryption techniques using OpenCV and numpy. It can be further extended and customized for different applications involving image encryption and privacy protection.

Feel free to modify and enhance the program to suit your specific needs.

