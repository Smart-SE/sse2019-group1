# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import requests
from take_photo_picam import take_photo
import os
import subprocess
import traceback
import logging
import boto3

logger = logging.getLogger(__name__)
fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)
TOKEN = None
with open('bebotte_token','r') as f:
    TOKEN = f.readlines()[0]

TOPIC = "IoT_Refrigerator/take_req"
HOSTNAME = "mqtt.beebotte.com"
PORT = 8883
CACERT = "mqtt.beebotte.com.pem"
PROFILE_NAME = "sse2019-group1"
SEND_COMMAND_TEMPLATE = "aws s3 cp {0} {1} --profile={2}"
DEBUG = True
s3 = boto3.resource('s3')

def send_img_to_s3(file_name, bucket_name):
    try:
      s3.Bucket(bucket_name).upload_file(file_name, file_name)
    except boto3.exceptions.S3UploadFialedError:
      logging.error("upload failed to S3")

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    logger.info('status {0}'.format(respons_code))
    client.subscribe(TOPIC)
    logger.info("start to subscribe: " + TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))["data"]
        if type(data) is str:
            # データが文字列で渡されてるので、そこだけ再度、オブジェクト化
            data = json.loads(data)
        else:
            data = data

        data = {key:value.strip() for key, value in data.items()}
        action = data['req_type']
        bucket_name = data['s3_bucket']
        logging.info("aciton='{0}', bucket_name='{1}'".format(action, bucket_name))
        if action == "take_photo":
            file_name = "tmp.jpeg"
            take_photo(file_name)
            if os.path.exists(file_name):
                send_img_to_s3(file_name, bucket_name)
            else:
                logging.error("failed to take photo")
        else:
            logging.warn(data)
    except:
        traceback.print_exc()
client = mqtt.Client()
client.username_pw_set("token:%s"%TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(CACERT)
client.connect(HOSTNAME, port=PORT, keepalive=60)
client.loop_forever()
