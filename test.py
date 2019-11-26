from PIL import Image
import pytesseract
import time
import keyboard
import random

IMAGE_INPUT_NAME = 'input.jpg'
FILE_OUTPUT_NAME = 'result.txt'
<<<<<<< HEAD
ACCEPTED_ASCII_LIST = []
for x in range(32, 127):
    ACCEPTED_ASCII_LIST.append(x)
=======
ACCEPTED_ASCII_LIST = [x for x in range(32, 127)]
>>>>>>> 7403bfc6c2f3985813e5bc962f07eec2be76b8d2
