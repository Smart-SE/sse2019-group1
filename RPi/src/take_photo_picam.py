# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import picamera
from datetime import datetime

def take_photo(file_name):
    try:
        #Take Picture
        camera = picamera.PiCamera()
        camera.capture(file_name)
    except KeyboardInterrupt:
        pass
    finally:
        camera.close()


    

if __name__ == "__main__":
    file_name = "{0}.jpeg".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    take_photo(file_name)
