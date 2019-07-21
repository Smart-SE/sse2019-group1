# how to use?

1. get models and python programs from pyimagesearch.com and unzip here.

https://www.pyimagesearch.com/2019/02/25/black-and-white-image-colorization-with-opencv-and-deep-learning/

2. change the source "show iamges" to "save image" in bw2_images.py

delete a paragraph started by this sentence.
`# show the original and output colorized images`

and add source is shown below.
`cv2.imwrite("tmp_colorized.jpg", colorized)`
