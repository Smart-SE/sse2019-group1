# -*- coding: utf-8 -*-

import numpy as np
import cv2
from datetime import datetime

dir_path = "./img/"

#Take Picture
cap = cv2.VideoCapture(0)
file_name = "{0}{1}.jpeg".format(dir_path, datetime.now().strftime("%Y%m%d%H%M%S"))
ret, frame = cap.read()
cv2.imwrite(file_name, frame)
cap.release()




