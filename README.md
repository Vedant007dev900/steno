# Image Steganography using Tkinter

## Overview
This project provides a GUI-based image steganography tool that allows users to hide a secret message inside an image and later extract it using a password. The project is built using Python with OpenCV and Tkinter.

## Features
- Hide a message inside an image.
- Protect hidden data with a password.
- Extract a message from an image using the correct password.
- Simple and user-friendly graphical interface.

## Dependencies
Ensure you have the following Python libraries installed:
```sh
pip install opencv-python numpy pillow tkinter
```

## How to Use
### Hiding a Message
1. Run the script: `python script.py`
2. Enter the secret message in the text box.
3. Set a password to protect the message.
4. Click on the "Hide Data" button.
5. Select an image file for embedding the message.
6. The modified image will be saved as `encryptedImage.png`.

### Extracting a Message
1. Run the script: `python script.py`
2. Enter the password used during message hiding.
3. Click on the "Extract Data" button.
4. Select the encrypted image.
5. If the password is correct, the hidden message will be displayed.

## Notes
- The message length is stored in the image to enable proper extraction.
- Ensure the selected image has enough pixels to store the message.
- Entering an incorrect password will result in an error.

## License
This project is open-source and available for modification and distribution.

