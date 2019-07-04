# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import picamera
from datetime import datetime

dir_path = "./img/"

def take_photo(file_name):
    try:
    
        #Take Picture
        camera = picamera.PiCamera()
        camera.capture(file_name)

    except KeyboardInterrupt:
        pass
    

if __name__ == "__main__":
    file_name = "{0}{1}.jpeg".format(dir_path, datetime.now().strftime("%Y%m%d%H%M%S"))
    take_photo(file_name)
