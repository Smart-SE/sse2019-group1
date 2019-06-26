# -*- coding: utf-8 -*-

import numpy as np
import RPi.GPIO as GPIO
import picamera
from datetime import datetime

dir_path = "./img/"

#Take Picture
camera = picamera.PiCamera()

try:
    file_name = "{0}{1}.jpeg".format(dir_path, datetime.now().strftime("%Y%m%d%H%M%S"))
    camera.capture(file_name)
    
except KeyboardInterrupt:
    pass
