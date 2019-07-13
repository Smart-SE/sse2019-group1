# -*- coding: utf-8 -*-
import picamera
from datetime import datetime
import logger as log


def take_photo(file_name: str) -> None:
    """take a photo with picamera

    Arguments:
        file_name {str} -- file name of taked photo
    """
    camera = None
    try:
        camera = picamera.PiCamera()
        camera.capture(file_name)
        log.Info(file_name)
    except Exception:
        log.Error("Failed to take a photo")
    finally:
        if not(camera is None):
            camera.close()


if __name__ == "__main__":
    file_name = "{0}.jpeg".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    take_photo(file_name)
