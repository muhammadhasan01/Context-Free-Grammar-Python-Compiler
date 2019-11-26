from PIL import Image
import pytesseract
import time
import keyboard
import random

IMAGE_INPUT_NAME = 'input.jpg'
FILE_OUTPUT_NAME = 'result.txt'

def extract_text_from_image():
    PIPE_ASCII = 124
