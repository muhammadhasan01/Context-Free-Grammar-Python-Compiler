from PIL import Image
import pytesseract
import time
import keyboard
import random


IMAGE_INPUT_NAME = 'input.jpg'
FILE_OUTPUT_NAME = 'result.txt'
ACCEPTED_ASCII_LIST = [x for x in range(32, 127)]
