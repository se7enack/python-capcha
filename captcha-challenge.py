#!//usr/bin/env python3

import os
import random
import string

from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
from playsound import playsound
from easygui import *


def askbox():
    user = enterbox("Enter the CAPTCHA below: ", image = img)
    if user == str(value):
        print("CAPTCHA Matches!")
    else:
        print("CAPTCHA Does NOT Match!")


def makecaptcha():
    global img
    img = 'out.png'
    image = ImageCaptcha()
    image.write(str(value), img)       
    

def saycaptcha():
    wav = 'out.wav'
    audio = AudioCaptcha()
    audio.write(str(value), wav)
    playsound(wav, False)


def generate():
    global value
    value = random.randrange(1000, 9999)   


generate()
makecaptcha()
saycaptcha()
askbox()
