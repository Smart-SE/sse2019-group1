#!/bin/sh
export VIRTUALENV=~/colorize/bw-colorization/.env/

while true;
do
  rm -rf tmp.jpg tmp_colorized.jpg
  python get_image.py
  python bw2color_image.py -i tmp.jpg -m ./model/colorization_release_v2.caffemodel -p ./model/colorization_deploy_v2.prototxt -c ./model/pts_in_hull.npy
  python post_image.py
done
